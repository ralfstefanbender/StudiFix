import React, { Component } from 'react'
import { makeStyles, Grid, Paper, Button, Typography, withStyles, Card, CardContent, CardActions, Divider} from '@material-ui/core';
import { Link as RouterLink } from 'react-router-dom';
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
      userName: null,
      friendRequests: null,
      groupRequests: null
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
          this.getFriendRequests(user.google_id);
          this.getUserGroupRequests(user.google_id)
        })
            }
  
  getFriendRequests = (google_id) => {
    StudyFixAPI.getAPI().getFriendRequestsByGoogleId(google_id).then(friendRequests =>
      this.setState({friendRequests: friendRequests.length})
    )}

  getUserGroupRequests = (google_id) => {
    StudyFixAPI.getAPI().getUserPendingGroupInvites(google_id).then(groupRequests =>
        this.setState({groupRequests: groupRequests.length})
    )}

  render(){  
    const { classes } = this.props;

    return (
      <Paper elevation={0} className={classes.root}>
        <div className={classes.content} align="center">
          <br margin-top='20px' />
          <Typography variant='h5' align="center">
            Welcome back {this.state.userName}
          </Typography>
          <br margin-top='20px' />
          <Divider />
          <br margin-top='20px' />
          <Grid>
            <Card variant='outlined' style={{width:"50%"}}>
              <CardContent>
                <Typography fontSize='14' color='primary' gutterBottom>
                  Freundschaftsanfragen
                </Typography>
                <Typography variant='body1' style={{textAlign:"center"}}>
                  Du hast <tag style={{color:"#f57c00"}}><b>{this.state.friendRequests}</b></tag> neue Anfrage(n)
                </Typography>
              </CardContent>
              <CardActions style={{justifyContent:"center"}}>
                <Button size='small' variant="contained" color='secondary' component={RouterLink} to={`/lernpartner`}>
                  Bring mich hin!
                </Button>
              </CardActions>
            </Card>
          </Grid>
          <Grid>
          <Card variant='outlined' style={{width:"50%"}}>
            <CardContent>
              <Typography fontSize='14' color='primary' gutterBottom>
                Gruppeneinladungen
              </Typography>
              <Typography variant='body1' style={{textAlign:"center"}}>
                Du hast <tag style={{color:"#f57c00"}}><b>{this.state.groupRequests}</b></tag> neue Gruppeneinladung(en)
              </Typography>
            </CardContent>
            <CardActions style={{justifyContent:"center"}}>
              <Button size='small' variant="contained" color='secondary' component={RouterLink} to={`/studygroup`}>
                Bring mich hin!
              </Button>
            </CardActions>
          </Card> 
          </Grid> 
        </div>
      </Paper>
    )
  }
}

export default withStyles(useStyles)(Overview);