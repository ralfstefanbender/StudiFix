import React, { Component } from 'react';
import { Typography, Grid, Button, withStyles, TextField, Collapse, IconButton, Divider } from '@material-ui/core';
import Alert from '@material-ui/lab/Alert';
import CloseIcon from '@material-ui/icons/Close';
import firebase from 'firebase/app';
import 'firebase/auth';
import UserProfile from '../pages/UserProfile';
import DeleteUserAccountDialog from '../dialogs/DeleteUserAccountDialog'
import StudyFixAPI from '../../api/StudyFixAPI';

/**
 * Beschreibt die Komponente für das Verändern des Profils und Lerprofils eines Users
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
                    userBO: UserBO,
                    newAdress: UserBO.getAdress(),
                    newFirstName: UserBO.getFirstName()

                }))
    }

    //** updaten des Users */
    updateUser = () => {
        var user = this.state.userBO
        user.setFirstName(this.state.newFirstName)
        user.setAdress(this.state.newAdress)
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

    //** Funktion für die Adressänderung eines Users */
    handleUserAdressChange = (event) => {
        this.setState({ newAdress: event.target.value })
    }

    //** Zeigt den Alert bei erfolgreicher Änderung der Daten an */
    setAlertOpen = (opened) => {
        this.setState({ alertOpen: opened })
    }

     /** Rendert die Komponente */
    render() {
        const person = this.state.userBO

        return (
            <Typography variant='h6' component='h1' align='center'>
                <Grid>
                    <br margin-top='20px' />

                Mein Konto
                <Divider />
                <Grid container spacing={3} justify="center"></Grid>
                    <br margin-top='20px' />

                    {person ?
                        <TextField
                            id="outlined-read-only-input1"
                            label="Name: "
                            onChange={this.handleUserNameChange}
                            defaultValue={person.getFirstName()}
                            InputProps={{
                                readOnly: false,
                            }}
                            variant="outlined"
                        />

                        : null}

                        <br margin-top='20px'></br>
                        <br></br>

                    {person ?
                        <TextField
                            id="outlined-read-only-input2"
                            label="Adresse: "
                            onChange={this.handleUserAdressChange}
                            defaultValue={person.getAdress()}
                            InputProps={{
                                readOnly: false,
                            }}
                            variant="outlined"
                        />

                        : null}
                        <br></br>
                        <br></br>
                    <Button style={{maxWidth:"30vh", minWidth:"30vh", maxHeight:"5vh", minHeight:"5vh"}} variant="outlined" color="secondary" onClick={() => this.state.newFirstName != "" && this.state.newFirstName != null && this.state.newAdress != null && this.state.newAdress != "" ? this.updateUser() : null}>Speichern</Button>
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
                            Daten wurden erfolgreich gespeichert!
                        </Alert>
                    </Collapse>
                    <br />
                    <br margin-top='20px' />
                    {person ? 
                        
                        
                        <DeleteUserAccountDialog user={person}/> : null }
                    <br />
                    <br margin-top='20px' />

                <Divider />
                

                    <br margin-top='20px' />
                <UserProfile/>
                </Grid>
            </Typography>

        )

    }

}

/** Component spezifische styles */
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