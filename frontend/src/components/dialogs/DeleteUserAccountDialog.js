import React, { Component } from 'react'
import Button from '@material-ui/core/Button';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';
import { ThemeProvider} from "@material-ui/core"
import Theme from "../../theme"
import StudyFixAPI from '../../api/StudyFixAPI';
import firebase from 'firebase/app';
import 'firebase/auth';
/**
 * @author  Dominic
 */
class DeleteUserAccountDialog extends Component {

  constructor(props) {
    super(props);
    this.state = {
      open: false,
      user: props.user
    }
  }

  handleClickOpen = () => {
    this.setState({ open: true });
  };

  handleClose = () => {
    this.setState({ open: false });
    
  };
  //** Löschen eines Users;//
  handleUserDelete = () => {
    StudyFixAPI.getAPI().deleteUser(this.state.user.getID()).then(
      firebase.auth().signOut()
    )
  }

  render() {
    return (
      <ThemeProvider theme={Theme}>

        <Button  style={{maxWidth:"30vh", minWidth:"30vh", maxHeight:"5vh", minHeight:"5vh", color:"red", outlinedcolor:"red"}} variant="outlined"  onClick={this.handleClickOpen}>
          Account löschen
        </Button>

        <Dialog open={this.state.open} onClose={this.handleClose} aria-labelledby="form-dialog-title">
          <DialogTitle id="form-dialog-title">Account löschen</DialogTitle>
          <DialogContent>
            <DialogContentText>
              Willst du deinen Account wirklich löschen ? 
            </DialogContentText>

          </DialogContent>

          <DialogActions>
            <Button onClick={this.handleUserDelete}>
              Ja
            </Button>
            <Button onClick={this.handleClose}>
              Nein
            </Button>
          </DialogActions>
        </Dialog>

      </ThemeProvider>
    )
  }
}

export default DeleteUserAccountDialog