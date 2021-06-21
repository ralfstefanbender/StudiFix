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



class CreateStudyGroup extends Component {


    constructor(props) {
      super(props);


      this.state = {
        creationDate: null,
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





    // Add Studygroup
     addStudyGroup = () => {
        let newStudyGroup = new StudyGroupBO();
        newStudyGroup.setDate(this.state.creationDate);
        newStudyGroup.setName(this.state.name);
        newStudyGroup.setChatId(this.state.chatidSelected);
        StudyFixAPI.getAPI().addStudyGroup(newStudyGroup).then(studygroupBO => {
            this.setState(this.baseState);
        }).catch(e =>
            this.setState({
                error: e
            }))

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
                    <Grid item>
                        <FormControl fullWidth required variant="outlined">
                            <InputLabel>Chat</InputLabel>
                            <Select name="chatidSelected" defaultValue="" label="Chat" onChange={this.handleSelectChange}>
                                {this.state.chats.map((chat) => (
                                        <MenuItem key={chat.getID()} value={chat.getID()}>{chat.getName()}</MenuItem>
                                    ))}
                            </Select>
                        </FormControl>
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