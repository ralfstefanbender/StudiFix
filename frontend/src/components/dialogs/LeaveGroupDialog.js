import React, { Component } from 'react'
import Button from '@material-ui/core/Button';
import Dialog from '@material-ui/core/Dialog';
import DeleteIcon from '@material-ui/icons/Delete';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';
import { ThemeProvider} from "@material-ui/core"
import Theme from "../../theme"
import RemoveIcon from '@material-ui/icons/Remove';
import StudyFixAPI from '../../api/StudyFixAPI';
import firebase from 'firebase/app';
import 'firebase/auth';


class LeaveGroupDialog extends Component {

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


  render() {
    console.log("props:", this.props)
    return (
      <ThemeProvider theme={Theme}>
        <Button startIcon={<DeleteIcon/>} size='small' color='primary' onClick={this.handleClickOpen}>
            Gruppe Verlassen
        </Button>
        <Dialog open={this.state.open} onClose={this.handleClose} aria-labelledby="form-dialog-title">
          <DialogTitle id="form-dialog-title">
              Gruppe Verlassen
          </DialogTitle>
          <DialogContent>
            <DialogContentText>
              Willst du die Gruppe wirklich verlassen?
            </DialogContentText>

          </DialogContent>

          <DialogActions>
            <Button  color='primary'>
              Ja
            </Button>
            <Button  color='primary' onClick={this.handleClose}>
              Nein
            </Button>
          </DialogActions>
        </Dialog>

      </ThemeProvider>
    )
  }
}

export default LeaveGroupDialog