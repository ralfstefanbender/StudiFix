import React, { Component } from 'react'
import Button from '@material-ui/core/Button';
import Dialog from '@material-ui/core/Dialog';
import DeleteIcon from '@material-ui/icons/Delete';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';
import { ThemeProvider} from "@material-ui/core";
import Theme from "../../theme";
import StudyFixAPI from '../../api/StudyFixAPI';
import firebase from 'firebase/app';
import 'firebase/auth';


class ShowBuddyProfileDialog extends Component {

    constructor(props) {
        super(props);
        this.state = {
          open: this.props.open,
          user: this.props.user,
          learningprofile: this.props.profileBO
        }
    }


    render() {
        return(
            <div>
            {this.state.learningprofile? 
            <Dialog open={this.state.open} onClose={this.props.handleClose} aria-labelledby="form-dialog-title">
                <DialogTitle id="form-dialog-title">
                    Learning Profile von {this.state.user.firstname}
                </DialogTitle>
                <DialogContent>
                    <DialogContentText>
                        <b>DegreeCourse:</b> {this.state.learningprofile.degree_course}<br/>
                        <b>Extroversion:</b> {this.state.learningprofile.extroversion}<br/>
                        <b>Frequency:</b> {this.state.learningprofile.frequency}<br/>
                        <b>Interests:</b> {this.state.learningprofile.interest}<br/>
                        <b>Learntype:</b> {this.state.learningprofile.learntyp}<br/>
                        <b>Previous Knowledge:</b> {this.state.learningprofile.prev_knowledge}<br/>
                        <b>Semester:</b> {this.state.learningprofile.semester}<br/>
                        <b>Study State:</b> {this.state.learningprofile.study_state}<br/>
                        
                    </DialogContentText>
                </DialogContent>
                <DialogActions>
                    <Button  color='primary' onClick={() => this.props.handleClose()}>
                        Close
                    </Button>
                </DialogActions>
            </Dialog>
            : null}
            </div>
        )
    }
}

export default ShowBuddyProfileDialog