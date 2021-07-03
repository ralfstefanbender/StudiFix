import React, { Component } from 'react'
import Button from '@material-ui/core/Button';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';
import { ThemeProvider, Grid, TextField, MenuItem} from "@material-ui/core";
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
          learningprofile: this.props.profileBO,
          newProfileName: this.props.profileBO.getName(),
          newDegreeCourse: this.props.profileBO.getDegreeCourse(),
          newInterest: this.props.profileBO.getInterest(),
          prev_knowledge: this.props.profileBO.getPrevKnowledge(),
          extroversion: this.props.profileBO.getExtroversion(),
          studystate: this.props.profileBO.getStudyState(),
          frequency: this.props.profileBO.getFrequency(),
          learntyp: this.props.profileBO.getLearntyp(),
          semester: this.props.profileBO.getSemester()
          
        }
    }
    // Value wird hier übergeben und setzt den state.prev_knowledge auf value
    handlePrevKnowlegeChange = (value) => {
        this.setState({ prev_knowledge: value })
          };
    // Value wird hier übergeben und setzt den state.extroversion auf value  
      handleExtroversionChange = (value) => {
        this.setState({ extroversion: value })
          };
    // Value wird hier übergeben und setzt den state.studystate auf value
      handleStudyStateChange = (value) => {
        this.setState({ studystate: value })
          };
    // Value wird hier übergeben und setzt den state.frequency auf value
      handleFrequencyChange = (value) => {
        this.setState({ frequency: value })
          };
    // Value wird hier übergeben und setzt den state.learntyp auf value
      handleLearntypChange = (value) => {
        this.setState({ learntyp: value })
          };
    // Value wird hier übergeben und setzt den state.semester auf value
      handleSemesterChange = (value) => {
        this.setState({ semester: value })
          };
    // ermöglicht das setzten einen neuen Profil Names
      handleProfileNameChange = (event) => {
        this.setState({ newProfileName: event.target.value })
        }
      // ermöglicht das setzten einer neuen Interesse
      handleInterestChange = (event) => {
        this.setState({ newInterest: event.target.value })
       }
       // ermöglicht das setzten eines neuen DeegreeCourses
      handleDegreeCourseChange = (event) => {
        this.setState({ newDegreeCourse: event.target.value })
       }


    render() {
      const profile = this.state.learningprofile

      const prev_knowledges = ['','Keine Vorkenntnisse','Geringe Vorkenntnisse','Mittelmäßige Vorkenntnisse','Gute Vorkenntnisse','Sehr gute Vorkenntnisse']
      
      const extroversions = ['','Sehr Introvertiert','Introvertiert','Etwas Introvertiert','Extrovertiert','Sehr Extrovertiert']
      
      const studystates = ['','Online','Offline']
      
      const frequencys = ['','1x im Monat','3x im Monat','1x die Woche','2x die Woche','4x die Woche']

      const learntyps = ['','Visueller Lerntyp', 'Auditiver Lerntyp', 'Haptischer Lerntyp', 'Kommunikativer Lerntyp', 'Gemischter Lerntyp']
          
      
      const semesters = ['',' 1. Semester',' 2. Semester',' 3. Semester',' 4. Semester', ' 5. Semester',' 6. Semester', ' 7. Semester',' 8. Semester', ' 9. Semester', ' 10. Semester', ' 11. Semester', ' 12. Semester' ]
        
        return(
            <div>
             
            <Dialog open={this.state.open} onClose={this.props.handleClose} aria-labelledby="form-dialog-title">
                <DialogTitle id="form-dialog-title">
                    Learning Profile von {this.state.user.firstname}
                </DialogTitle>
                <DialogContent>
                <Grid container spacing={2} justify="center">
            <Grid item xs={4}>
            {profile ?
                <div>
                <b>Profilname:</b><br/>{this.state.newProfileName}

                </div>

                : null}
                </Grid>
                
                <Grid item xs={4}>  
            {profile ?
                <div>
                <b>Interessiert in:</b><br/>{this.state.newInterest}

                </div>

                : null}
                </Grid>
                
                <br/>
                <br/>
                <Grid item xs={4}>
                {profile ?
                <div>
                <b>Studiengang:</b><br/>{this.state.newDegreeCourse}

                </div>

                : null}
                </Grid>
                <br></br>
                <br></br>
                <Grid item xs={4}>
                                {profile ?
                                <div>
                                <b>Vorkenntnisse:</b><br/>{prev_knowledges[this.state.prev_knowledge]}

                                </div>
                                : null}
                                </Grid>
                                

                                <br></br>
                                <br></br>
                                <Grid item xs={4}>
                                {profile ?
                                <div>
                                <b>Extrovertiertheit:</b><br/>{extroversions[this.state.extroversion]}

                                </div>
                                
                                : null}
                                </Grid>
                                

                                <br></br>
                                <br></br>
                                <Grid item xs={4}>
                                {profile ?
                                <div>
                                <b>Lernpräferenz:</b><br/>{studystates[this.state.studystate]}

                                </div>
                                : null}
                                </Grid>
                            
                                <br></br>
                                <br></br>
                                <Grid item xs={4}>
                                {profile ?
                                <div>
                                <b>Frequenz:</b><br/>{frequencys[this.state.frequency]}

                                </div>
                                : null}
                                </Grid>

                                <br></br>
                                <br></br>
                                <Grid item xs={4}>
                                {profile ?
                                <div> 
                                <b>Lerntyp:</b><br/>{learntyps[this.state.learntyp]}

                                </div>
                                : null}
                                </Grid>

                                <br></br>
                                <br></br>
                                <Grid item xs={4}>
                                {profile ?
                                <div>
                                <b>Semester:</b><br/>{semesters[this.state.semester]}
                                
                                </div>
                                : null}
                                </Grid>
                                </Grid>
                </DialogContent>
                <DialogActions>
                    <Button  color='primary' onClick={() => this.props.handleClose()}>
                        Close
                    </Button>
                </DialogActions>
            </Dialog>
            
            </div>
        )
    }
}

export default ShowBuddyProfileDialog