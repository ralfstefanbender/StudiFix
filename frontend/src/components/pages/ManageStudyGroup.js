import React, { Component } from 'react';
import {withStyles, Grid, Button, Typography, Divider} from '@material-ui/core';
import { StudyFixAPI } from '../../api';
import ContextErrorMessage from '../dialogs/ContextErrorMessage';
import LoadingProgress from '../dialogs/LoadingProgress';
import CreateStudyGroup from './CreateStudyGroup';
import StudyGroupDetail from '../subcomponents/StudyGroupDetail';
import firebase from "firebase";
import GroupsUserGroupRequests from "../subcomponents/GroupsUserGroupRequests";

/**
 * Übersichtsseite der StudyGroups
 */

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
      userBO: null
    };

  }

  //** Einmaliges aufrufen nach dem Rendering */
  componentDidMount() {
    this.getUserByGoogleId();
  }

  //** Fetch den User und setzt ihn in den State  */
  getUserByGoogleId = () => {
    StudyFixAPI.getAPI().getUserByGoogleId(firebase.auth().currentUser.uid).then((user)=>{
          this.setState({userBO:user});
          this.getAllStudyGroups(user.google_id);
          this.getUserGroupRequests(user.google_id)
        })
            }

  //** Holt alle Anfragen für Gruppen aus dem Backend  */
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

  //** Holt StudyGroups des eingeloggten Users aus dem Backend  */
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

    //** Setzt den state von loading auf true */
    this.setState({
      loadingInProgress: true,
      loadingError: null
    });
  }

    //**  Öffnet beim klicken auf eine Studygroup das Dialogfenster */
    openstudygroup(){
        this.setState({
            openpr: true });

    }


    //** Schließt beim klicken auf eine Studygroup das Dialogfenster */
    closestudygroup= () => {
      this.setState({openpr:false});
    }

    //**  Öffnet das MobileMenu */
    handleMobileMenu = (event) => {
      this.setState({
        mobileAnchorEl: event.currentTarget,
      })
    }

    //**  Schließt  das MobileMenu */
    handleMobileClose = () => {
      this.setState({
        mobileAnchorEl: null
      })
    }

    //**  Aktualisiert die Seite beim Annehmen einer Anfrage  */
    reload = () => {
      this.getAllStudyGroups(this.state.userBO.google_id)
    }

    
  /** Rendert die Komponente */
  render() {
    const { classes } = this.props;
    const { studygroups, grouprequests, loadingInProgress, loadingError } = this.state;

    return (
      <div className={classes.root}>
         < CreateStudyGroup reload={this.reload}
           {...this.props}
           ManageStudyGroup ={ManageStudyGroup}
           openpr={this.state.openpr}
           openstudygroup={this.openstudygroup}
           closestudygroup={this.closestudygroup}

              />

        <br margin-top='20px' />
        <div align="center">
          <Button variant="contained" color="secondary" onClick={() => {this.openstudygroup(); this.handleMobileClose()}}>
            Neue Lerngruppe erstellen
          </Button>
        </div>
        <br margin-top='20px' />
            <Typography variant='h6' component='h1' align='center'>
              Deine Gruppen
            </Typography>
            <Divider />
          <Grid>
            {
            studygroups.map(studygroups => <StudyGroupDetail reload={this.reload} key={studygroups.getID()} {...this.props}
            nameID={studygroups.getName()}  ID={studygroups.getID()} />)
            }
          </Grid>
          <br margin-top='20px' />
          {grouprequests.length > 1 &&
          <Typography variant='h6' component='h1' align='center'>
             <b style={{color:"#f57c00"}}>{grouprequests.length}</b> Leute möchten deiner Gruppe beitreten!
            </Typography>
          }
          {grouprequests.length == 1 &&
          <Typography variant='h6' component='h1' align='center'>
              <b style={{color:"#f57c00"}}>{grouprequests.length}</b> Person möchte deiner Gruppe beitreten!
            </Typography>
          }
            <Divider />
          <Grid>
            {
            grouprequests.map(friendRequests => <GroupsUserGroupRequests key={friendRequests.getID()} {...this.props}
            firstName={friendRequests.getFirstName()} lastName={friendRequests.getLastName()} ID={friendRequests.getID()} 
            groupId={friendRequests.getGroupId()} groupName={friendRequests.getGroupname()} />)
            }
            <LoadingProgress show={loadingInProgress} />
            <ContextErrorMessage error={loadingError} contextErrorMsg={`Die Anfragen konnten nicht geladen werden`} />
          </Grid>
          <LoadingProgress show={loadingInProgress} />
          <ContextErrorMessage error={loadingError} contextErrorMsg={`Die Liste der Gruppen konnte nicht geladen werden`} />
      </div>
    );
  }
}

/** Component spezifische styles */
const styles = theme => ({
  root: {
    width: '100%',
  }
});



export default withStyles(styles)(ManageStudyGroup);
