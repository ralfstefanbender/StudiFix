import React, {Component} from 'react';
import PropTypes from 'prop-types';
import { withStyles, Typography, Card, CardActions, CardContent, Button, CardActionArea  } from '@material-ui/core';
import { StudyFixAPI } from '../../api';
import ContextErrorMessage from '../dialogs/ContextErrorMessage';
import LeaveGroupDialog from '../dialogs/LeaveGroupDialog';
import LoadingProgress from '../dialogs/LoadingProgress';



class StudyGroupDetail extends Component{

    constructor(props){
        super(props);

        // Init state

        this.state = {
            loadingInProgress: false,
            loadingError: null,
            learningProfile: null
      };
    }


/** Renders the component */
render() {
    const { classes, ID, nameID} = this.props;
    const {  loadingInProgress, loadingError} = this.state;

    return (
      <Card variant='outlined' className={classes.root}>
        <CardActionArea>
          <CardContent>
            <Typography variant='h6' component='h2'>
            {nameID}
            </Typography>
            <Typography variant='body2' component='p'>
              ID: {ID}
            </Typography>
          </CardContent>
        </CardActionArea>
          <CardActions style={{float: 'right'}}>
            <LeaveGroupDialog groupId={ID} />
          </CardActions>

        <LoadingProgress show={loadingInProgress} />
        <ContextErrorMessage error={loadingError} contextErrorMsg={`The data could not be loaded.`} onReload={this.getLearningProfileUserById} />
      </Card>
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

});

export default withStyles(styles)(StudyGroupDetail);