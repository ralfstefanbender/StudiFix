import React, {Component} from 'react';
import PropTypes from 'prop-types';
import { withStyles, Typography, Card, CardActions, CardContent, Button  } from '@material-ui/core';
import { StudyFixAPI } from '../../api';
import ContextErrorMessage from '../dialogs/ContextErrorMessage';
import LoadingProgress from '../dialogs/LoadingProgress';


class UserGroupsDetail extends Component{

    constructor(props){
        super(props);
        
        // Init state
        
        this.state = {
            loadingInProgress: false,
            loadingError: null,
      };
    }

/** Renders the component */
render() {
    const { classes, ID, firstName, lastName } = this.props;
    const {  loadingInProgress, loadingError } = this.state;

    return (
      <Card variant='outlined' className={classes.root}>
        <CardContent>
          <Typography variant='h6'>
            Buddy:
          </Typography>
          <Typography >
            Vorname: {firstName} <br></br>
            Nachname: {lastName} <br></br> 
            ID: {ID}
          </Typography>
          <CardActions>
            <Button size='small' color='primary'>Optionen</Button>
          </CardActions>
        </CardContent>

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
  accountEntry: {
    fontSize: theme.typography.pxToRem(15),
    flexBasis: '33.33%',
    flexShrink: 0,
  }
});

export default withStyles(styles)(UserGroupsDetail);