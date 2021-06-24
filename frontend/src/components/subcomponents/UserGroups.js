import React, { Component } from 'react'
import { withStyles, Button, Grid, Typography, Divider } from '@material-ui/core';
import PropTypes from 'prop-types';
import { StudyFixAPI } from '../../api';
import { Link as RouterLink } from 'react-router-dom';
import ContextErrorMessage from '../dialogs/ContextErrorMessage';
import LoadingProgress from '../dialogs/LoadingProgress';
import UserGroupsDetail from './UserGroupsDetail';
import UserGroupsFriendRequests from './UserGroupsFriendRequests';
import firebase from 'firebase/app';




class UserGroups extends Component {
  constructor(props){
    super(props);

    this.state = {
      buddys: [],
      friendRequests: [],
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

  }

  getUserByGoogleId = () => {
    StudyFixAPI.getAPI().getUserByGoogleId(firebase.auth().currentUser.uid).then((user)=>{
          this.setState({userBO:user}); 
          this.getFriends(user.google_id);
          this.getFriendRequests(user.google_id)
        })
            }

  /** Fetches ChatInvitationBOs for current user */
  getFriends = (google_id) => {
    StudyFixAPI.getAPI().getFriendsByGoogleId(google_id).then(buddys =>
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

  getFriendRequests = (google_id) => {
    StudyFixAPI.getAPI().getFriendRequestsByGoogleId(google_id).then(friendRequests =>
      this.setState({
        friendRequests: friendRequests,
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
  const { buddys, friendRequests, loadingInProgress, loadingError} = this.state;

  return(
    <div className={classes.root}>
      < br/>
        {
        //<Button variant="contained" color='secondary' component={RouterLink} to={`/matching_page`}>
        //Nach neuen Lernpartnern Suchen
        //</Button>
        }
        
          <Typography variant='h6' component='h1' align='center'>
              Your Buddies
            </Typography>
            <Divider />

          <Grid>
            {
            buddys.map(buddys => <UserGroupsDetail key={buddys.getID()} {...this.props}
            firstName={buddys.getFirstName()} lastName={buddys.getLastName()} ID={buddys.getID()}
            adress={buddys.getAdress()} />)
            }
          </Grid>

          <br margin-top='20px' />
          <Typography variant='h6' component='h1' align='center'>
              Your Friend Requests
            </Typography>
            <Divider />

          <Grid>
            {
            friendRequests.map(friendRequests => <UserGroupsFriendRequests key={friendRequests.getID()} {...this.props}
            firstName={friendRequests.getFirstName()} lastName={friendRequests.getLastName()} ID={friendRequests.getID()} />)
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