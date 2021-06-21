import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { withStyles, Grid, Button } from '@material-ui/core';
import { StudyFixAPI } from '../../api';
import ContextErrorMessage from '../dialogs/ContextErrorMessage';
import LoadingProgress from '../dialogs/LoadingProgress';
import CreateStudyGroup from './CreateStudyGroup';

/**
 * Shows all accounts of the bank.
 *
 * @author [Christoph Kunz](https://github.com/christophkunz)
 */
class ManageStudyGroup extends Component {

  constructor(props) {
    super(props);

    // Init an empty state
    this.state = {
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
    this.getAllStudyGroups();
  }

  /** gets the account list for this account */
  getAllStudyGroups = () => {
    StudyFixAPI.getAPI().getAllStudyGroups().then(studygroups =>
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



    // opens project
    openProject(){
        this.setState({
            openpr: true });

    }
    // close project
    closeProject = () => {
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
    const { studygroups, loadingInProgress, loadingError } = this.state;

    return (
      <div className={classes.root}>
         < CreateStudyGroup
           {...this.props}
           ManageStudyGroup ={ManageStudyGroup}
           openpr={this.state.openpr}
           openProject={this.openProject}
           closeProject={this.closeProject}

              />


       <Button onClick={() => {this.openProject(); this.handleMobileClose()}}>Add project</Button>
          {
            studygroups.map(studygroup => <StudyGroupDetail key={studygroup.getID()} {...this.props}
            nameID={studygroup.getName()} ID={studygroup.getID()} />)
          }

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
