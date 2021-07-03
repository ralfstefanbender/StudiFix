import React, {Component} from 'react';
import { withStyles, Typography, Card, CardActions, CardContent, Button, CardActionArea  } from '@material-ui/core';
import { StudyFixAPI } from '../../api';
import ClearIcon from '@material-ui/icons/Clear';
import CheckIcon from '@material-ui/icons/Check';
import ContextErrorMessage from '../dialogs/ContextErrorMessage';
import LoadingProgress from '../dialogs/LoadingProgress';

//** Nutzer anfragen für Gruppen die der current user hat */
class GroupsUserGroupRequests extends Component{

    constructor(props){
        super(props);

        // Init state

        this.state = {
            loadingInProgress: false,
            loadingError: null,
            disabled:false,
            colorStyle: {}
      };
    }

    //** Gruppenanfrage annehmen */
    acceptGroupRequest = (e, group_id, user_id) =>{
      StudyFixAPI.getAPI().acceptGroupRequest(group_id, user_id).then(() => {this.setState({disabled:true}); this.setState({colorStyle: {backgroundColor:"#90EE90"}})})
    }

    //** Gruppenanfrage ablehnen */
    declineGroupRequest = (e, group_id, user_id) =>{
      StudyFixAPI.getAPI().declineGroupRequest(group_id, user_id).then(() => {this.setState({disabled:true}); this.setState({colorStyle: {backgroundColor:"#F08080"}})})
    }

/** Renders the component */
render() {
    const { classes, ID, firstName, lastName, groupName, groupId } = this.props;
    const {  loadingInProgress, loadingError } = this.state;

    return (
      <Card variant='outlined' className={classes.root} style={this.state.colorStyle}>
        <CardActionArea>
          <CardContent>
            <Typography variant='h6' component='h2'>
                {firstName} {lastName} <b style={{color:"#f57c00"}}>möchte</b> {groupName} <b style={{color:"#f57c00"}}>beitreten</b>
            </Typography>
          </CardContent>
        </CardActionArea>
          <CardActions style={{float: 'right'}}>
            <Button disabled={this.state.disabled} startIcon={<CheckIcon/>} size='small' color='primary' onClick={(e)=>{this.acceptGroupRequest(e, groupId, ID)}}>Anfrage Annehmen</Button>
            <Button disabled={this.state.disabled} startIcon={<ClearIcon/>} size='small' color='primary' onClick={(e)=>{this.declineGroupRequest(e, groupId, ID)}}>Anfrage Ablehnen</Button>
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

export default withStyles(styles)(GroupsUserGroupRequests);