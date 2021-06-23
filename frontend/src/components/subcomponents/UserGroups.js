import React, { Component } from 'react'
import { makeStyles, withStyles, Button, Link, Grid, List, Paper, Typography, } from '@material-ui/core';
import PropTypes from 'prop-types';
import { StudyFixAPI } from '../../api';
import { Link as RouterLink } from 'react-router-dom';
import ContextErrorMessage from '../dialogs/ContextErrorMessage';
import LoadingProgress from '../dialogs/LoadingProgress';
import UserGroupsDetail from './UserGroupsDetail';
import firebase from 'firebase/app';




class UserGroups extends Component {
  constructor(props){
    super(props);

    this.state = {
      buddys: [],
      acceptedBuddys: [],
      acceptedInvites: [],
      openpr:false,
      loadingInProgress: false,
      loadingError: null,
      redirect: false,
      error: null,
      openDialog: false,
      userBO: null,
    };
  }

  /** Lifecycle method, which is called when the component gets inserted into the browsers DOM */
  componentDidMount() {
    this.getUserByGoogleId();
    this.getAllUsers();

  }

  /** Fetches ChatInvitationBOs for current user */
  getAllUsers = () => {
    StudyFixAPI.getAPI().getAllUsers().then(buddys =>
      this.setState({
        buddys: buddys,
        loadingInProgress: false,
        error: null
    })).catch(e => this.setState({
      loadingInProgress: false,
      loadingError: e
    }));

    this.setState({
      loadingInProgress: true,
      loadingError: null
    });
  }

  getAcceptedUsers = () => {
    console.log(this.state.userBO.id)
    StudyFixAPI.getAPI().getChatInvitationAcceptedInvitesTarget(this.state.userBO.id).then((acc) => this.setState({acceptedInvites:acc}))
    StudyFixAPI.getAPI().getChatInvitationAcceptedInvitesSource(this.state.userBO.id).then((acc) => this.setState({acceptedInvites:acc}))
    
  }

  getUserByGoogleId = () => {
    StudyFixAPI.getAPI().getUserByGoogleId(firebase.auth().currentUser.uid)
        .then((user)=>{
          this.setState({userBO:user})
          this.getAcceptedUsers()
        })
            }

   // opens usergroups
   openusergroups(){
    this.setState({
        openpr: true });

    }
    // close usergroups
    closeusergroups= () => {
        this.setState({openpr:false});
    }

    handleMobileMenu = (event) => {
      this.setState({
        mobileAnchorEl: event.currentTarget,
      })
    }

    handleMobileClose = () => {
      this.setState({
        mobileAnchorEl: null
      })
    }


render(){
  const { classes,} = this.props;
  const { buddys, loadingInProgress, loadingError} = this.state;

  return(
    <div className={classes.root}>
      < br/>
        <Button variant="contained" color='secondary' component={RouterLink} to={`/matching_page`}>
          Nach neuen Lernpartnern Suchen
        </Button>
          <Grid>
            {
            buddys.map(buddys => <UserGroupsDetail key={buddys.getID()} {...this.props}
            firstName={buddys.getFirstName()} lastName={buddys.getLastName()} ID={buddys.getID()} />)
            }
          </Grid>

          <LoadingProgress show={loadingInProgress} />
          <ContextErrorMessage error={loadingError} contextErrorMsg={`The list could not be loaded.`} />
      </div>
    );
  }
}




/** Component specific styles */
const styles = theme => ({
  root: {
    width: '100%',
  },
});

/** PropTypes */
UserGroups.propTypes = {
  /** @ignore */
  classes: PropTypes.object.isRequired,
}

export default withStyles(styles)(UserGroups);