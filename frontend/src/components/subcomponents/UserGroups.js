import React, { Component } from 'react'
import { makeStyles, withStyles, Box, Button, Paper, Typography, Link, Grid } from '@material-ui/core';
import PropTypes from 'prop-types';
import { StudyFixAPI } from '../../api';
import ContextErrorMessage from '../dialogs/ContextErrorMessage';
import LoadingProgress from '../dialogs/LoadingProgress';
import UserGroupsDetail from './UserGroupsDetail';



class UserGroups extends Component {
  constructor(props){
    super(props);

    this.state = {
      buddys: [],
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
       <Button onClick={() => {this.openusergroups(); this.handleMobileClose()}}>LernPartner hinzufügen</Button>
          {
            buddys.map(buddys => <UserGroupsDetail key={buddys.getID()} {...this.props}
            firstName={buddys.getFirstName()} lastName={buddys.getLastName()} ID={buddys.getID()} />)
          }

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
  }
});


/** PropTypes */
UserGroups.propTypes = {
  /** @ignore */
  classes: PropTypes.object.isRequired,
}

export default withStyles(styles)(UserGroups);