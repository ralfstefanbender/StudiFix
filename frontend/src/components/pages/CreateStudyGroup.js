import React, {Component} from 'react';
import {DialogContent, DialogActions, ThemeProvider, Dialog, DialogTitle, TextField, Button } from'@material-ui/core';
import {StudyFixAPI, StudyGroupBO, ChatBO} from '../../api';
import Theme from "../../theme";
import firebase from "firebase";



class CreateStudyGroup extends Component {


    constructor(props) {
      super(props);


      this.state = {
        creationDate: null,
        current_user:null,
        name:'',
        openpr:null,
        studygroups:[],
        chatid: null,
        chatidSelected:null,
       
        value:null,
        chats:[],
        notShowDrop: false,
        error:null
      }

      this.baseState = this.state;

    }


    getAllStudyGroups = () => {
        StudyFixAPI.getAPI().getAllStudyGroups()
        .then(studygroupBOs =>
            this.setState({
               studygroups: studygroupBOs,
               error: null
            })).catch(e =>
                this.setState({
                    studygroups:[],
                    error: e
                }))
    }


     show = () =>{
              this.setState({
                  notShowDrop: true,
              });
              }


    getCurrentUser(){
    StudyFixAPI.getAPI().getUserByGoogleId(firebase.auth().currentUser.uid).then((user) => {this.setState({current_user:user})})
    }

    // Add Studygroup
     addStudyGroup = () => {
        StudyFixAPI.getAPI().createStudyGroupPackage(this.state.name,this.state.current_user.google_id).then(() => {this.props.closestudygroup(); this.props.reload()})
    }


    getAllChats = () => {
        StudyFixAPI.getAPI().getAllChats()
        .then(chatBOs =>{
            this.setState({
                chats: chatBOs,
                error: null
            });
        }).catch(e =>
                this.setState({
                    chats:[],
                    error: e
                }))
    }

   componentDidMount(){
        this.getCurrentUser();
        this.getAllStudyGroups();
        this.getAllChats();
    }


    handleChange = (e) =>{
        this.setState({
            [e.target.id]: e.target.value
        });
    }

   handleChangeNum = (e) =>{
        this.setState({
            [e.target.id]: parseInt(e.target.value, 10)
        });
    }


    handleSelectChange = (e) =>{
        this.setState({
            [e.target.name]: e.target.value
        });
    }

     closestudygroup = () => {
        this.setState({openpr:false});
    }


 render(){

        const { chats, studygroups } = this.state;
        const {classes}= this.props;

    return(
        <ThemeProvider theme={Theme}>
            <Dialog open={this.props.openpr} onClose={this.props.closestudygroup}>
                <DialogTitle id="form-dialog-title">
                    Lerngruppe erstellen
                </DialogTitle>
                    <DialogContent>
                        <TextField required variant="outlined" id="name" label="Name:" onChange={this.handleChange} value={this.state.name}/>
                    </DialogContent>
                    <DialogActions>
                        <Button variant="contained" color="secondary" onClick={this.addStudyGroup}>
                            Erstellen
                        </Button>
                        <Button color='primary' onClick={this.props.closestudygroup}>
                            Zurück
                        </Button>
                    </DialogActions>      
            </Dialog>
          </ThemeProvider>
    );
}
}


export default CreateStudyGroup;
