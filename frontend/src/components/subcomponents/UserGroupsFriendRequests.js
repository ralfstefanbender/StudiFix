import React, {Component} from 'react';
import { withStyles, Typography, Card, CardActions, CardContent, Button, CardActionArea  } from '@material-ui/core';
import { StudyFixAPI } from '../../api';
import ClearIcon from '@material-ui/icons/Clear';
import CheckIcon from '@material-ui/icons/Check';
import ContextErrorMessage from '../dialogs/ContextErrorMessage';
import LoadingProgress from '../dialogs/LoadingProgress';

/**
 * Beschreibt die Komponente zum Anzeigen  der Usereinladungen
 */

class UserGroupsFriendRequests extends Component{

    constructor(props){
        super(props);
               
        this.state = {
            loadingInProgress: false,
            loadingError: null,
            disabled:false,
            colorStyle: {}
      };
    }

    //** Akzeptiert die Chateinladung beim Annehmen der Anfrage und lädt die Seite neu */
    acceptChatInvite = (e, user_id) =>{
      StudyFixAPI.getAPI().acceptFriendRequest(this.props.userBO.id, user_id).then(() => {this.setState({disabled:true}); this.setState({colorStyle: {backgroundColor:"#90EE90"}}); this.props.reload()})
    }

    //** Lehnt die Chateinladung ab  */
    declineChatInvite = (e, user_id) =>{
      StudyFixAPI.getAPI().declineFriendRequest(this.props.userBO.id, user_id).then(() => {this.setState({disabled:true}); this.setState({colorStyle: {backgroundColor:"#F08080"}})})  
    }

    /** Rendert die Komponente */
    render() {
        const { classes, ID, firstName, lastName } = this.props;
        const {  loadingInProgress, loadingError } = this.state;

        return (
          <Card variant='outlined' className={classes.root} style={this.state.colorStyle}>
            <CardActionArea>
              <CardContent>
                <Typography variant='h6' component='h2'>
                    {firstName} {lastName}
                </Typography>
              </CardContent>
            </CardActionArea>
              <CardActions style={{float: 'right'}}>
                <Button disabled={this.state.disabled} startIcon={<CheckIcon/>} size='small' color='primary' onClick={(e)=>{this.acceptChatInvite(e, ID)}}>Anfrage Annehmen</Button>
                <Button disabled={this.state.disabled} startIcon={<ClearIcon/>} size='small' color='primary' onClick={(e)=>{this.declineChatInvite(e, ID)}}>Anfrage Ablehnen</Button>
              </CardActions>
            
            <LoadingProgress show={loadingInProgress} />
            <ContextErrorMessage error={loadingError} contextErrorMsg={`The data could not be loaded.`} onReload={this.getLearningProfileUserById} />
          </Card>
        );
      }
    }

    /** Component spezifische styles */
    const styles = theme => ({
      root: {
        width: '100%',
        padding: theme.spacing(1),
        marginTop: theme.spacing(1)
      },
      
    });

export default withStyles(styles)(UserGroupsFriendRequests);