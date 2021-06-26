import React, { Component } from 'react';
import PropTypes from 'prop-types';
import {withStyles, Grid, Button, Typography, Divider} from '@material-ui/core';
import { StudyFixAPI } from '../../api';
import ContextErrorMessage from '../dialogs/ContextErrorMessage';
import LoadingProgress from '../dialogs/LoadingProgress';
import CreateStudyGroup from './CreateStudyGroup';
import StudyGroupDetail from '../subcomponents/StudyGroupDetail';
import firebase from "firebase";
import UserGroupsDetail from "../subcomponents/UserGroupsDetail";
import UserGroupsFriendRequests from "../subcomponents/UserGroupsFriendRequests";
import GroupsUserGroupRequests from "../subcomponents/GroupsUserGroupRequests";


class ManageStudyGroup extends Component {

  constructor(props) {
    super(props);

    // Init an empty state
    this.state = {
      current_user: null,
      grouprequests: [],
      studygroups: [],
      openpr:false,
      loadingInProgress: false,
      loadingError: null,
      redirect: false,
      error: null,
      openDialog: false,
    };

  }



  
  /** Lifecycle method, which is called when the component gets inserted into the browsers DOM */
  componentDidMount() {
    this.getUserByGoogleId();
  }

  getUserByGoogleId = () => {
    StudyFixAPI.getAPI().getUserByGoogleId(firebase.auth().currentUser.uid).then((user)=>{
          this.setState({userBO:user});
          this.getAllStudyGroups(user.google_id);
          this.getUserGroupRequests(user.google_id)
        })
            }

  getUserGroupRequests = (google_id) => {
    StudyFixAPI.getAPI().getUserPendingGroupInvites(google_id).then((grouprequests) =>{
       this.setState({
           grouprequests: grouprequests,
           loadingInProgress: false,
           loadingError: null
      })}).catch(e =>
        this.setState({ // Reset state with error from catch
          loadingInProgress: false,
          loadingError: e
        })
      );
  }

  /** gets the account list for this account */
  getAllStudyGroups = (google_id) => {
    StudyFixAPI.getAPI().getGroupsByGoogleId(google_id).then(studygroups =>
      this.setState({
        studygroups: studygroups,
        loadingInProgress: false, // loading indicator
        loadingError: null
      })).catch(e =>
        this.setState({ // Reset state with error from catch
          loadingInProgress: false,
          loadingError: e
        })
      );

    // set loading to true
    this.setState({
      loadingInProgress: true,
      loadingError: null
    });
  }



    // opens studygroup
    openstudygroup(){
        this.setState({
            openpr: true });

    }
    // close studygroup
    closestudygroup= () => {
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


  /** Renders the component */
  render() {
    const { classes } = this.props;
    const { studygroups, grouprequests, loadingInProgress, loadingError } = this.state;

    return (
      <div className={classes.root}>
         < CreateStudyGroup
           {...this.props}
           ManageStudyGroup ={ManageStudyGroup}
           openpr={this.state.openpr}
           openstudygroup={this.openstudygroup}
           closestudygroup={this.closestudygroup}

              />

        <br margin-top='20px' />
        <bruh_moment><Button variant="contained" color="secondary" onClick={() => {this.openstudygroup(); this.handleMobileClose()}}>Create new Studygroup</Button></bruh_moment>
            <Typography variant='h6' component='h1' align='center'>
              Your Groups
            </Typography>
            <Divider />
          
          <Grid>
            {
            studygroups.map(studygroups => <StudyGroupDetail key={studygroups.getID()} {...this.props}
            nameID={studygroups.getName()}  ID={studygroups.getID()} />)
            }
          </Grid>
          <br margin-top='20px' />
          <Typography variant='h6' component='h1' align='center'>
              New people want to join your Group!
            </Typography>
            <Divider />

          <Grid>
            {
            grouprequests.map(friendRequests => <GroupsUserGroupRequests key={friendRequests.getID()} {...this.props}
            firstName={friendRequests.getFirstName()} lastName={friendRequests.getLastName()} ID={friendRequests.getID()} 
            groupId={friendRequests.getGroupId()} groupName={friendRequests.getGroupname()} />)
            }
            <LoadingProgress show={loadingInProgress} />
            <ContextErrorMessage error={loadingError} contextErrorMsg={`The Requestlist could not be loaded.`} />
          </Grid>
          <LoadingProgress show={loadingInProgress} />
          <ContextErrorMessage error={loadingError} contextErrorMsg={`The list of all studygroups not be loaded.`} />
      </div>
    );
  }
}

/** Component specific styles */
const styles = theme => ({
  root: {
    width: '100%',
  }
});



export default withStyles(styles)(ManageStudyGroup);
