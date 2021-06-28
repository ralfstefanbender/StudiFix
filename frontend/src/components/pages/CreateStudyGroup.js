import React, {Component} from 'react';
import {
    MenuItem,
    Dialog,
    DialogTitle,
    Select,
    InputLabel,
    TextField,
    FormControl,
    Typography,
    Slider,
    Button,
    Grid} from'@material-ui/core';
import {StudyFixAPI, StudyGroupBO, ChatBO} from '../../api';
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

        <Dialog open={this.props.openpr} onClose={this.props.closestudygroup} fullWidth maxWidth='md'>
          <DialogTitle fontcolor='primary' >Create Studygroup</DialogTitle>
            <Grid container spacing={2} justify="center" driection="row"  >

                <Grid container item direction="column"  xs={6} md={6} spacing={2}>
                    <Grid item>
                        <TextField fullWidth required variant="outlined" id="name" label="Name:" onChange={this.handleChange} value={this.state.name}/>
                    </Grid>
                 </Grid>
                  <Grid container spacing={2} justify="center" driection="row"  >


                <Grid item>
                    <Button variant="outlined" onClick={this.props.closestudygroup}>Cancel</Button>
                </Grid>
                <Grid item>
                    <Button variant="contained" color="primary"
                    onClick={this.addStudyGroup}>Submit</Button>
                </Grid>
                </Grid>


                </Grid>






          </Dialog>

    );
 }


}




export default CreateStudyGroup;
