import React, {Component} from 'react';
import {Dialog,
    DialogTitle,
    MenuItem,
    Select,
    InputLabel,
    TextField,
    RadioGroup,
    FormControl,
    FormControlLabel,
    Radio,
    Button,
    Grid,
    Typography} from'@material-ui/core';
import {withStyles} from '@material-ui/core';
import {StudyFixAPI, StudyGroupBO} from '../api';


class CreateStudyGroup extends Component {


    constructor(props) {
      super(props);


      this.state = {
        creationDate: null,
        name:'',
        prev_knowledge: null,
        extroverison: null,
        study_state: null,
        frequency: null,
        learntyp: null,
        semester: null,
        interest : null,
        degree_course : null,
        group_id: null,
        studygroups:[],
        chat_id: null,
        chatidSelected:null,
        studygroupSelected:null,
        chats:[],


        modules: [],
        openpr:null,
        moduleSelected: null,
        edvNumber: null,
        projecttypes: [],
        projecttype: {},
        ptSelected: null,
        numSpots: null,
        professors: [],
        additionalProf: null,
        prof:null,
        weekly: false,
        specialRoom: false,
        desiredRoom: null,
        shortDescription: '',
        language: '',
        externalPartner: null,
        numBlockdaysPriorLecture: null,
        numBlockdaysDuringLecture: null,
        dateDuringLecture: null,
        numBlockdaysInExam: null,
        error: null,
        notShowDrop: null,
        spots: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
            15 , 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
            28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
      }


      this.baseState = this.state;



    }




    getAllStudyGroups = () => {
        StudyFixAPI.getAPI().getAllStudyGroups()
        .then(studygroupBOs =>
            this.setState({
               studygroup: studygroupBOs,
               error: null
            })).catch(e =>
                this.setState({
                    studygroups:[],
                    error: e
                }))
    }





    componentDidMount(){
        this.getAllStudyGroups();
        this.getAllChats();
    }

    // Add a new Project
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





 render(){
    const { classes } = this.props;


    return(

        <Dialog open={this.props.openpr} onClose={this.props.closeStudyGroup} fullWidth maxWidth='md'>
            <DialogTitle fontcolor='primary' className={classes.dialogHeader}>SUBMIT PROJECT</DialogTitle>
            <Grid container spacing={2} justify="center" driection="row" className={classes.grid} >

                <Grid container item direction="column" xs={12} md={6} spacing={2}>
                    <Grid item>
                        <TextField fullWidth required variant="outlined" id="name" label="Name:" onChange={this.handleChange} value={this.state.name}/>
                    </Grid>
                    <Grid item>
                        <FormControl fullWidth required variant="outlined" className={classes.FormControl}>
                            <InputLabel>Module</InputLabel>
                            <Select name="chatidSelected" defaultValue="" label="Chat" onChange={this.handleSelectChange}>
                                {this.state.chats.map((chat) => (
                                        <MenuItem key={chat.getID()} value={chat.getID()}>{chat.getName()}</MenuItem>
                                    ))}
                            </Select>
                        </FormControl>
                    </Grid>
                        <Grid item>
                        <FormControl fullWidth required variant="outlined" className={classes.FormControl}>
                            <InputLabel>StudyGroups</InputLabel>
                            <Select name="studygroupSelected" defaultValue="" label="Studygroup" onChange={this.handleSelectChange}>
                                {this.state.studygoups.map((studygroup) => (
                                        <MenuItem key={studygroup.getID()} value={studygroup.getID()}>{studygroup.getName()}</MenuItem>
                                    ))}
                            </Select>
                        </FormControl>
                    </Grid>
                 </Grid>
                <Grid item>
                    <Button variant="outlined" onClick={this.props.closeStudyGroup}>Cancel</Button>
                </Grid>
                <Grid item>
                    <Button variant="contained" color="primary" onClick={this.addStudyGroup}>Submit</Button>
                </Grid>

            </Grid>
        </Dialog>
    );
 }


}

const styles = theme => ({
    grid:{
        width: '100%',
        margin: '0px',
        padding: '20px'
    },
    dialogHeader:{
        textAlign: "center"
    }
});


export default withStyles(styles)(CreateStudyGroup);