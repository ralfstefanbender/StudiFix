import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { withStyles, Typography, Paper } from '@material-ui/core';
import { StudyFixAPI } from '../../api';
import ContextErrorMessage from '../dialogs/ContextErrorMessage';
import LoadingProgress from '../dialogs/LoadingProgress';


class StudyGroupDetail extends Component {

  constructor(props) {
    super(props);

    // Init state
    this.state = {

      loadingInProgress: false,
      loadingError: null,
    };
  }

  /** Lifecycle method, which is called when the component gets inserted into the browsers DOM */


  /** Renders the component */
  render() {
    const { classes, ID, nameID } = this.props;
    const {  loadingInProgress, loadingError } = this.state;

    return (
      <Paper variant='outlined' className={classes.root}>

        <Typography variant='h6'>
          Studygroup
        </Typography>
        <Typography >
          Name: {nameID}
          ID: {ID}
        </Typography>


        <LoadingProgress show={loadingInProgress} />
        <ContextErrorMessage error={loadingError} contextErrorMsg={`The data of customer id could not be loaded.`} onReload={this.getLearningProfileUserById} />
      </Paper>
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
  accountEntry: {
    fontSize: theme.typography.pxToRem(15),
    flexBasis: '33.33%',
    flexShrink: 0,
  }
});



export default withStyles(styles)(StudyGroupDetail);