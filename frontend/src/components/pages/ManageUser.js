import React, { Component } from 'react';
import { Typography, Grid, Button, withStyles } from '@material-ui/core';
import { Divider } from '@material-ui/core'
import { TextField, Collapse, IconButton } from '@material-ui/core'
import Alert from '@material-ui/lab/Alert';
import CloseIcon from '@material-ui/icons/Close';
import firebase from 'firebase/app';
import 'firebase/auth';
import DeleteUserAccountDialog from '../dialogs/DeleteUserAccountDialog'
import StudyFixAPI from '../../api/StudyFixAPI';
/**
 * @author Dominic
 */

class ManageUser extends Component {
    constructor(props) {
        super(props)

        this.state = {
            userBO: null,
            newFirstName: null,
            newLastName: null,
            newAdress: null,
            alertOpen: false

        }
    }
    //** Einmaliges aufrufen nach dem Rendering */
    componentDidMount() {
        this.getUserByGoogleId()
    }
    //** Fetch den User aus dem Backend */
    getUserByGoogleId = () => {
        StudyFixAPI.getAPI().getUserByGoogleId(firebase.auth().currentUser.uid)
            .then(UserBO =>
                this.setState({
                    userBO: UserBO
                }))
    }
    //** updaten des Users */
    updateUser = () => {
        var user = this.state.userBO
        user.setFirstName(this.state.newFirstName)
       //** */ user.setLastName(this.state.newLastName)
       //** */ user.setAdress(this.newAdress)
        StudyFixAPI.getAPI().updateUser(user)
            .then(function () {
                this.setAlertOpen(true);
                StudyFixAPI.getAPI().getUserById(user.getID())
                    .then(UserBO =>
                        this.setState({
                            userBO: UserBO
                        }),

                    )
            }.bind(this))


    }

    

    //** Funktion für die Namensändeurng eines Users */
    handleUserNameChange = (event) => {
        this.setState({ newFirstName: event.target.value })
    }

    setAlertOpen = (opened) => {
        this.setState({ alertOpen: opened })
    }

    render() {
        const person = this.state.userBO

        return (
            <Typography variant='h6' component='h1' align='center'>
                <Grid>
                    <br margin-top='20px' />

                Mein Konto
                <Divider />

                    <br margin-top='20px' />

                    {person ?
                        <TextField
                            id="outlined-read-only-input"
                            label="Name: "
                            onChange={this.handleUserNameChange}
                            defaultValue={person.getFirstName()}
                            InputProps={{
                                readOnly: false,
                            }}
                            variant="outlined"
                        />

                        : null}

                    <Button onClick={() => this.state.newFirstName != "" && this.state.newFirstName != null ? this.updateUser() : console.log("da stimmt was ned")}>Speichern</Button>
                    <Collapse in={this.state.alertOpen}>
                        <Alert
                            action={
                                <IconButton
                                    aria-label="close"
                                    color="inherit"
                                    size="small"
                                    onClick={() => {
                                        this.setAlertOpen(false);
                                    }}
                                >
                                    <CloseIcon fontSize="inherit" />
                                </IconButton>
                            }
                        >
                            Du heißt jetzt {this.state.newFirstName}!
                        </Alert>
                    </Collapse>
                    <br />
                    <br margin-top='20px' />
                    {person ? 
                        
                        
                        <DeleteUserAccountDialog user={person}/> : null }
                    <br />
                    <br margin-top='20px' />

                
                    Learningprofile
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
  
export default withStyles(styles)(ManageUser);