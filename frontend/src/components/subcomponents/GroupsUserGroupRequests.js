import React, {Component} from 'react';
import { withStyles, Typography, Card, CardActions, CardContent, Button, CardActionArea  } from '@material-ui/core';
import { StudyFixAPI } from '../../api';
import ClearIcon from '@material-ui/icons/Clear';
import CheckIcon from '@material-ui/icons/Check';
import ContextErrorMessage from '../dialogs/ContextErrorMessage';
import LoadingProgress from '../dialogs/LoadingProgress';


class GroupsUserGroupRequests extends Component{

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
        <CardActionArea>
          <CardContent>
            <Typography variant='h6' component='h2'>
                {firstName} {lastName}
            </Typography>
            <Typography variant='body2' component='p'>
              ID: {ID}
            </Typography>
          </CardContent>
        </CardActionArea>
          <CardActions style={{float: 'right'}}>
            <Button startIcon={<CheckIcon/>} size='small' color='primary'>Anfrage Annehmen</Button>
            <Button startIcon={<ClearIcon/>} size='small' color='primary'>Anfrage Ablehnen</Button>
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

export default withStyles(styles)(GroupsUserGroupRequests);