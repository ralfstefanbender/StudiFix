import React, {Component} from 'react';
import PropTypes from 'prop-types';
import { withStyles, Typography, Card, CardActions, CardContent, Button, CardActionArea  } from '@material-ui/core';
import { StudyFixAPI } from '../../api';
import ContextErrorMessage from '../dialogs/ContextErrorMessage';
import LeaveGroupDialog from '../dialogs/LeaveGroupDialog';
import ShowGroupProfileDialog from '../dialogs/ShowGroupProfileDialog';
import StudyGroupProfileDialog from '../dialogs/StudyGroupProfileDialog';
import LoadingProgress from '../dialogs/LoadingProgress';


//** Conmponent für Studygroups in denen der User ist */
class StudyGroupDetail extends Component{

    constructor(props){
        super(props);

        // Init state

        this.state = {
            loadingInProgress: false,
            loadingError: null,
            learningProfile: null,
            open: false
      };
    }

    //** Das Learningprofile der Gruppe aufrufen*/
    componentDidMount(){
      StudyFixAPI.getAPI().getLearningProfileGroupByGroupId(this.props.ID).then((profile) => {
        this.setState({learningProfile:profile});
      })
    }

    //** Dialog Öffnen */
    handleClickOpen = () => {
      this.setState({ open: true });
    };
    
    //** Dialog schließen */
    handleClose = () => {
      this.setState({ open: false });      
    };


/** Renders the component */
render() {
    const { classes, ID, nameID} = this.props;
    const {  loadingInProgress, loadingError} = this.state;

    return (
      <Card variant='outlined' className={classes.root}>
        <CardActionArea onClick={() => this.handleClickOpen()}>
          <CardContent>
            <Typography variant='h6' component='h2'>
            {nameID}
            </Typography>
          </CardContent>
        </CardActionArea>
        {this.state.open? <ShowGroupProfileDialog  profileBO={this.state.learningProfile} open={this.state.open} handleClose={this.handleClose}></ShowGroupProfileDialog>: false}
          <CardActions style={{float: 'right'}}>
          <StudyGroupProfileDialog groupId={ID} />
          <LeaveGroupDialog reload={() => this.props.reload()} groupId={ID} />

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