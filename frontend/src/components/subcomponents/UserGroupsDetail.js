import React, {Component} from 'react';
import { withStyles, Typography, Card, CardActions, CardContent, CardActionArea  } from '@material-ui/core';
import ContextErrorMessage from '../dialogs/ContextErrorMessage';
import DeleteBuddyDialog from '../dialogs/DeleteBuddyDialog';
import LoadingProgress from '../dialogs/LoadingProgress';
import { StudyFixAPI } from '../../api';
import ShowBuddyProfileDialog from '../dialogs/ShowBuddyProfileDialog';


class UserGroupsDetail extends Component{

    constructor(props){
        super(props);
        
        // Init state
        
        this.state = {
            loadingInProgress: false,
            loadingError: null,
            userBO: this.props.userBO,
            learningprofileBO: null,
            open: false
      };
    }

componentDidMount(){
  StudyFixAPI.getAPI().getLearningProfileUserByUserId(this.state.userBO.id).then((profile) => {
    this.setState({learningprofileBO:profile});
    console.log(profile)
  })
}

handleClickOpen = () => {
  this.setState({ open: true });
};

handleClose = () => {
  this.setState({ open: false });      
};

/** Renders the component */
render() {
    const { classes, ID, adress, firstName, lastName, email} = this.props;
    const {  loadingInProgress, loadingError} = this.state;

    return (
      <Card variant='outlined' className={classes.root}>
        <CardActionArea onClick={() => this.handleClickOpen()}>
          <CardContent>
            <Typography variant='h6' component='h2'>
            {firstName} {lastName}
            </Typography>
            <Typography variant='body2' component='p' >
              ID: {ID} <br />
              E-mail: {email} <br />
              Adress: {adress}
            </Typography>
          </CardContent>
        </CardActionArea>
            {this.state.open? <ShowBuddyProfileDialog user={this.state.userBO} profileBO={this.state.learningprofileBO} open={this.state.open} handleClose={this.handleClose}></ShowBuddyProfileDialog>: false}        
          <CardActions style={{float: 'right'}}>
            <DeleteBuddyDialog buddyId ={ID} />   
          </CardActions>
        
        <LoadingProgress show={loadingInProgress} />
        <ContextErrorMessage error={loadingError} contextErrorMsg={`The data could not be loaded.`} onReload={this.getLearningProfileUserById} />
      </Card>
    );
  }
}

/** Component specific styles */
const styles = theme => ({
  root: {
    width: '100%',
    padding: theme.spacing(1),
    marginTop: theme.spacing(1)
  },
  
});

export default withStyles(styles)(UserGroupsDetail);