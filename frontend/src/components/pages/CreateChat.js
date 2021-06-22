aimport React, {Component} from 'react';
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
import {StudyFixAPI,ChatBO} from '../../api';



class CreateStudyGroup extends Component {


    constructor(props) {
      super(props);


      this.state = {
        creationDate: null,
        name:'',
        chatid: null,

        error:null
      }


      this.baseState = this.state;


    }







     show = () =>{
              this.setState({
                  notShowDrop: true,
              });
              }





    // Add Chat
     addChat = () => {
        let newChat = new ChatBO();
         newChat.setDate(this.state.creationDate);
         newChat.setName(this.state.name);

        StudyFixAPI.getAPI().addChat(newChat).then(chatBO => {
            this.setState(this.baseState);
        }).catch(e =>
            this.setState({
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

     closechat = () => {
        this.setState({openpr:false});
    }






 render(){

        const {chat} = this.state;
        const {classes}= this.props;

    return(

        <Dialog open={this.props.openpr} onClose={this.props.closeschat} fullWidth maxWidth='md'>
          <DialogTitle fontcolor='primary' >Create chat</DialogTitle>
            <Grid container spacing={2} justify="center" driection="row"  >

                <Grid container item direction="column"  xs={6} md={6} spacing={2}>
                    <Grid item>
                        <TextField fullWidth required variant="outlined" id="name" label="Name:" onChange={this.handleChange} value={this.state.name}/>
                    </Grid>
                    <Grid item>
                        <FormControl fullWidth required variant="outlined">
                            <InputLabel>Chat</InputLabel>

                        </FormControl>
                    </Grid>

                 </Grid>
                  <Grid container spacing={2} justify="center" driection="row"  >


                <Grid item>
                    <Button variant="outlined" onClick={this.props.closeschat}>Cancel</Button>
                </Grid>
                <Grid item>
                    <Button variant="contained" color="primary"
                    onClick={this.addChat}>Submit</Button>
                </Grid>
                </Grid>


                </Grid>






          </Dialog>

    );
 }


}




export default CreateChat;
