import React, { Component } from 'react'
import { makeStyles, Paper, Typography, withStyles} from '@material-ui/core';
import StudyFixAPI from '../../api/StudyFixAPI';
import firebase from 'firebase/app';

const useStyles = makeStyles(theme => ({
  root: {
    width: '100%',
    marginTop: theme.spacing(2),
    marginBottom: theme.spacing(2),
    padding: theme.spacing(1)
  },
  content: {
    margin: theme.spacing(1),
  }
}));

class Overview extends Component {
  constructor(props){
    super(props);

    this.state = {
      userBO: null,
      userName: null
    };
  }


  componentDidMount(){
    StudyFixAPI.getAPI().getAuth();
    this.getUserByGoogleId()
  }

  getUserByGoogleId = () => {
    StudyFixAPI.getAPI().getUserByGoogleId(firebase.auth().currentUser.uid).then((user)=>{
          this.setState({userBO:user}); 
          this.setState({userName:user.getFirstName()});
        })
            }


  render(){  
    const { classes } = this.props;

    return (
      <Paper elevation={0} className={classes.root}>
        <div className={classes.content}>
          <br margin-top='20px' />
          <Typography variant='h6' align="center">
            Welcome back {this.state.userName}
          </Typography>
        </div>
      </Paper>
    )
  }
}

export default withStyles(useStyles)(Overview);