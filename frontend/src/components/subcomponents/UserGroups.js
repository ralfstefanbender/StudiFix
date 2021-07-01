import React, { Component } from 'react'
import { withStyles, Grid, Typography, Divider } from '@material-ui/core';
import PropTypes from 'prop-types';
import { StudyFixAPI } from '../../api';
import ContextErrorMessage from '../dialogs/ContextErrorMessage';
import LoadingProgress from '../dialogs/LoadingProgress';
import UserGroupsDetail from './UserGroupsDetail';
import DeleteBuddyDialog from '../dialogs/DeleteBuddyDialog';
import UserGroupsFriendRequests from './UserGroupsFriendRequests';
import firebase from 'firebase/app';
import { set } from 'date-fns';


class UserGroups extends Component {
  constructor(props){
    super(props);

    this.state = {
      buddys: [],
      friendRequests: [],
      openpr:false,
      loadingInProgress: false,
      loadingError: null,
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

  /** Fetches Friends for current user */
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

  /** Fetches Friend Invites for current user */
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

    reload = () => {
      this.getFriends(this.state.userBO.google_id)
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
              Deine Buddies
            </Typography>
            <Divider />

          <Grid>
            {
            buddys.map(buddys => <UserGroupsDetail reload={this.reload} key={buddys.getID()}
            firstName={buddys.getFirstName()} lastName={buddys.getLastName()} email={buddys.getEMail()} ID={buddys.getID()}
            adress={buddys.getAdress()} userBO={buddys} />)
            }
            <LoadingProgress show={loadingInProgress} />
            <ContextErrorMessage error={loadingError} contextErrorMsg={`Deine Buddys konnten nicht geladen werden`} />
          </Grid>
          <br margin-top='20px' />
        {friendRequests.length > 1 &&
          <Typography variant='h6' component='h1' align='center'>
              Du hast <tag style={{color:"#f57c00"}}><b>{friendRequests.length}</b></tag> Freundschaftsanfragen
            </Typography>
        }
        {friendRequests.length == 1 &&
          <Typography variant='h6' component='h1' align='center'>
              Du hast <tag style={{color:"#f57c00"}}><b>{friendRequests.length}</b></tag> Freundschaftsanfrage
            </Typography>
        }
        <Divider />
          <Grid>
            {
            friendRequests.map(friendRequests => <UserGroupsFriendRequests reload={this.reload} key={friendRequests.getID()} userBO={this.state.userBO}
            firstName={friendRequests.getFirstName()} lastName={friendRequests.getLastName()} ID={friendRequests.getID()} />)
            }
            <LoadingProgress show={loadingInProgress} />
            <ContextErrorMessage error={loadingError} contextErrorMsg={`Die Anfragenliste konnte nicht geladen werden`} />
          </Grid>
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