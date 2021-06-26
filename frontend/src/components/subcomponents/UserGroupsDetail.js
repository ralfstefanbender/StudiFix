import React, {Component} from 'react';
import { withStyles, Typography, Card, CardActions, CardContent, CardActionArea  } from '@material-ui/core';
import ContextErrorMessage from '../dialogs/ContextErrorMessage';
import DeleteBuddyDialog from '../dialogs/DeleteBuddyDialog';
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
    const { classes, ID, adress, firstName, lastName } = this.props;
    const {  loadingInProgress, loadingError} = this.state;

    return (
      <Card variant='outlined' className={classes.root}>
        <CardActionArea>
          <CardContent>
            <Typography variant='h6' component='h2'>
            {firstName} {lastName}
            </Typography>
            <Typography variant='body2' component='p' >
              ID: {ID} <br />
              Adress: {adress}
            </Typography>
          </CardContent>
        </CardActionArea>
          <CardActions style={{float: 'right'}}>
            <DeleteBuddyDialog buddyId ={ID} />   
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

export default withStyles(styles)(UserGroupsDetail);