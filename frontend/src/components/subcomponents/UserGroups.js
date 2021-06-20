import React, { Component } from 'react'
import { makeStyles, withStyles, Paper, Typography, Link, Grid } from '@material-ui/core';
import PropTypes from 'prop-types';
import LoadingProgress from '../dialogs/LoadingProgress';
import StudyFixAPI from '../../api/StudyFixAPI';


class UserGroups extends Component {
  constructor(props){
    super(props);

    this.state = {
      buddys: [],
      loadingInProgress: false,
      error: null
    };
  }

  /** Fetches ChatInvitationBOs for current user */
  getChatInvitationAcceptedInvitesSource = (suser) => {
    StudyFixAPI.getAPI().getChatInvitationAcceptedInvitesSource(suser)
    .then(chatInvitationBOs => this.setState({
      buddys: chatInvitationBOs,
      filteredBuddys: [...chatInvitationBOs],
      loadingInProgress: false,
      error: null
    })).catch(e => this.setState({
      buddys: [],
      loadingInProgress: false,
      error: e
    }));

    this.setState({
      loadingInProgress: true,
      error: null
    });
  }

/** Lifecycle method, which is called when the component gets inserted into the browsers DOM */
componentDidMount() {
  this.getChatInvitationAcceptedInvitesSource();
}

render(){
  const { classes,} = this.props;
  const { buddys, loadingInProgress, error} = this.state;

  return(
    <div className = {classes.root}>
        <h1>Hier stehen ihre Lernpartner:</h1>
    </div>
  )
}

}



const styles = theme => ({
  root: {
    width: '100%',
    marginTop: theme.spacing(2),
    marginBottom: theme.spacing(2),
    padding: theme.spacing(1)
  },
  content: {
    margin: theme.spacing(1),
  }
});


export default withStyles(styles)(UserGroups);