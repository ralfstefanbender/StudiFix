import React, { Component } from 'react';
import { Typography, Grid, Button, withStyles } from '@material-ui/core';
import { Divider } from '@material-ui/core'
import { TextField, Collapse, IconButton } from '@material-ui/core'
import Alert from '@material-ui/lab/Alert';
import CloseIcon from '@material-ui/icons/Close';
import firebase from 'firebase/app';
import 'firebase/auth';
import StudyFixAPI from '../../api/StudyFixAPI';
/**
 * @author Dominic
 */

class UserProfile extends Component {
    constructor(props) {
        super(props)

        this.state = {
            UserBO: null,
            UserProfileBO: null,
        }
    }

    componentDidMount(){
      this.getUserByGoogleId()
    }

    getUserByGoogleId = () => {
      StudyFixAPI.getAPI().getUserByGoogleId(firebase.auth().currentUser.uid).then((user)=>{
        this.setState({userBO:user});
        this.getLearningProfileUserById(user.getID()) 
      })
          }

    getLearningProfileUserById = (UserId) => {
      StudyFixAPI.getAPI().getLearningProfileUserById(UserId)
        .then(UserProfileBO =>
            console.log(UserProfileBO))
    }



  render(){
    const profile = this.state.UserProfileBO

    return (
    <Typography variant='h6' component='h1' align='center'>
        <Grid>
            <br margin-top='20px' />

        Mein Profil
        <Divider />

            <br margin-top='20px' />

            {profile ?
                <TextField
                    id="outlined-read-only-input"
                    label="PrevKnowledge "
                    onChange={this.handleUserNameChange}
                    defaultValue={profile.getPrevKnowledge()}
                    InputProps={{
                        readOnly: false,
                    }}
                    variant="outlined"
                />

                : null}

                <br margin-top='20px'></br>
                <br></br>

            {profile ?
                <TextField
                    id="outlined-read-only-input"
                    label="Adresse: "
                    onChange={this.handleUserAdressChange}
                    defaultValue={profile.getExtroversion()}
                    InputProps={{
                        readOnly: false,
                    }}
                    variant="outlined"
                />

                : null}
                <br></br>
                <br></br>
            

        <Divider />

            <br margin-top='20px' />

        </Grid>
    </Typography>

    )

  }

}

const styles = theme => ({
  root: {
    width: '100%',
    marginTop: theme.spacing(2),
    marginBottom: theme.spacing(2),
    padding: theme.spacing(1)
  },
  content: {
    margin: theme.spacing(1),
  }
});

export default withStyles(styles)(UserProfile);