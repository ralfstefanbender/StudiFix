import React, { Component } from 'react';
import { Typography, Grid, Button, withStyles, Divider, TextField } from '@material-ui/core';
import firebase from 'firebase/app';
import MenuItem from '@material-ui/core/MenuItem';
import 'firebase/auth';
import StudyFixAPI from '../../api/StudyFixAPI';

/**
 * Beschreibt die Komponente zum Verändern des Lernprofils
 */

class UserProfile extends Component {
    constructor(props) {
        super(props)

        this.state = {
            UserBO: null,
            UserProfileBO: null,
            prev_knowledge: null,
            extroversion: null,
            studystate: null,
            frequency: null,
            learntyp: null,
            semester: null,
            newProfileName: null,
            newDegreeCourse: null,
            newInterest: null,
        }
    }

    //** Einmaliges aufrufen nach dem Rendering */
    componentDidMount(){
      this.getUserByGoogleId()
    }

    //** Fetch den User aus dem Backend */
    getUserByGoogleId = () => {
      StudyFixAPI.getAPI().getUserByGoogleId(firebase.auth().currentUser.uid).then((user)=>{
        this.setState({userBO:user});
        this.getLearningProfileUserByUserId(user.getID()) 
      })
          }

    //** Holt das Lernprofil des Users aus dem Backend */
    getLearningProfileUserByUserId = (UserId) => {
      StudyFixAPI.getAPI().getLearningProfileUserByUserId(UserId)
        .then(UserProfileBO =>
          this.setState({
              UserProfileBO: UserProfileBO,
              newProfileName: UserProfileBO.getName(),
              newDegreeCourse: UserProfileBO.getDegreeCourse(),
              newInterest: UserProfileBO.getInterest(),
              prev_knowledge: UserProfileBO.getPrevKnowledge(),
              extroversion: UserProfileBO.getExtroversion(),
              studystate: UserProfileBO.getStudyState(),
              frequency: UserProfileBO.getFrequency(),
              learntyp: UserProfileBO.getLearntyp(),
              semester: UserProfileBO.getSemester(),

              

          }))
}

//** Lädt die Veränderungen des Lernprofils ins Backend */
updateProfile = () => {
  var profile = this.state.UserProfileBO
  profile.setName(this.state.newProfileName)
  profile.setInterest(this.state.newInterest)
  profile.setDegreeCourse(this.state.newDegreeCourse)
  profile.setPrevKnowledge(this.state.prev_knowledge)
  profile.setExtroversion(this.state.extroversion)
  profile.setStudyState(this.state.studystate)
  profile.setFrequency(this.state.frequency)
  profile.setLearntyp(this.state.learntyp)
  profile.setSemester(this.state.semester)
  StudyFixAPI.getAPI().updateLearningProfileUser(profile)
      .then(function () {
          StudyFixAPI.getAPI().getLearningProfileUserById(profile.getID())
              .then(UserProfileBO =>
                  this.setState({
                      UserProfileBO: UserProfileBO
                  }),

              )
      }.bind(this))


}
    //** Setzt die Änderung des Vorwissens in den State */
    handlePrevKnowlegeChange = (value) => {
      this.setState({ prev_knowledge: value })
        };

    //** Setzt die Änderung der Extrovertiertheit in den State */
    handleExtroversionChange = (value) => {
      this.setState({ extroversion: value })
        };

    //** Setzt die Änderung der Lernpräferenz in den State */
    handleStudyStateChange = (value) => {
      this.setState({ studystate: value })
        };

    //** Setzt die Änderung der Lernfrequenz in den State */
    handleFrequencyChange = (value) => {
      this.setState({ frequency: value })
        };

    //** Setzt die Änderung des Lerntyps in den State */
    handleLearntypChange = (value) => {
      this.setState({ learntyp: value })
        };

    //** Setzt die Änderung des Semesters in den State */
    handleSemesterChange = (value) => {
      this.setState({ semester: value })
        };

    //** Setzt die Änderung des Profilnamens in den State */
    handleProfileNameChange = (event) => {
      this.setState({ newProfileName: event.target.value })
      }

    //** Setzt die Änderung der Interesse in den State */
    handleInterestChange = (event) => {
      this.setState({ newInterest: event.target.value })
     }

    //** Setzt die Änderung des Studiengangs in den State */
    handleDegreeCourseChange = (event) => {
      this.setState({ newDegreeCourse: event.target.value })
     }
    
  /** Rendert die Komponente */
  render(){

    const profile = this.state.UserProfileBO

    const {classes} = this.props

    const prev_knowledges = [
      {
          value: 1,
          label: 'Keine Vorkenntnisse',
      },
      {
          value: 2,
          label: 'Geringe Vorkenntnisse',
      },
      {
          value: 3,
          label: 'Mittelmäßige Vorkenntnisse',
      },
      {
          value: 4,
          label: 'Gute Vorkenntnisse',
      },
      {
          value: 5,
          label: 'Sehr gute Vorkenntnisse',
      },
  ];

  const extroversions = [
    {
        value: 1,
        label: 'Sehr Introvertiert',
    },
    {
        value: 2,
        label: 'Introvertiert',
    },
    {
        value: 3,
        label: 'Etwas Introvertiert',
    },
    {
        value: 4,
        label: 'Extrovertiert',
    },
    {
        value: 5,
        label: 'Sehr Extrovertiert',
    },
];

const studystates = [
  {
      value: 1,
      label: 'Online',
  },
  {
      value: 2,
      label: 'Offline',
  },
];

const frequencys = [
  {
      value: 1,
      label: '1x im Monat',
  },
  {
      value: 2,
      label: '3x im Monat',
  },
  {
      value: 3,
      label: '1x die Woche',
  },
  {
      value: 4,
      label: '2x die Woche',
  },
  {
      value: 5,
      label: '4x die Woche',
  },
];

const learntyps = [
  {
      value: 1,
      label: 'Visueller Lerntyp',
  },
  {
      value: 2,
      label: 'Auditiver Lerntyp',
  },
  {
      value: 3,
      label: 'Haptischer Lerntyp',
  },
  {
      value: 4,
      label: 'Kommunikativer Lerntyp',
  },
  {
      value: 5,
      label: 'Gemischter Lerntyp',
  },
];

const semesters = [
  {
      value: 1,
      label: ' 1. Semester',
  },
  {
      value: 2,
      label: ' 2. Semester',
  },
  {
      value: 3,
      label: ' 3. Semester',
  },
  {
      value: 4,
      label: ' 4. Semester',
  },
  {
      value: 5,
      label: ' 5. Semester',
  },
  {
    value: 6,
    label: ' 6. Semester',
},
{
    value: 7,
    label: ' 7. Semester',
},
{
    value: 8,
    label: ' 8. Semester',
},
{
    value: 9,
    label: ' 9. Semester',
},
{
    value: 10,
    label: ' 10. Semester',
},
{
  value: 11,
  label: ' 11. Semester',
},
{
  value: 12,
  label: ' 12. Semester',
},
];


    return (
    
    <Typography variant='h6' component='h1' align='center'>
        <Grid>
            <br margin-top='20px' />

        Mein Profil
        <Divider />

            <br margin-top='20px' />
            <Grid container spacing={3} justify="center">
            <Grid item xs={4}>
            {profile ?
                <TextField style={{maxWidth:"30vh", minWidth:"30vh"}}
                    id="standard-basic1"
                    label="Profile Name "
                    onChange={this.handleProfileNameChange}
                    defaultValue={profile.getName()}
                    InputProps={{
                        readOnly: false,
                    }}
                    
                />

                : null}
                </Grid>
                
                <Grid item xs={4}>  
            {profile ?
                <TextField style={{maxWidth:"30vh", minWidth:"30vh"}}
                    id="standard-basic2"
                    label="Interessiert in "
                    onChange={this.handleInterestChange}
                    defaultValue={profile.getInterest()}
                    InputProps={{
                        readOnly: false,
                    }}
                    
                />

                : null}
                </Grid>
                
                <br/>
                <br/>
                <Grid item xs={4}>
                {profile ?
                <TextField style={{maxWidth:"30vh", minWidth:"30vh"}}
                    id="standard-basic3"
                    label="Studiengang "
                    onChange={this.handleDegreeCourseChange}
                    defaultValue={profile.getDegreeCourse()}
                    InputProps={{
                        readOnly: false,
                    }}
                    
                />

                : null}
                </Grid>
                <br></br>
                <br></br>
                <Grid item xs={4}>
                                {profile ?
                                <TextField style={{maxWidth:"30vh", minWidth:"30vh"}}
                              
                                    id="standard-select-currency"
                                    select
                                    label="Vorkenntnisse"
                                    onChange={(event) => this.handlePrevKnowlegeChange(event.target.value)}
                                    defaultValue={profile.getPrevKnowledge()}
                                    helperText="Bitte wählen sie ihre Vorkenntnisse"
                                >
                                    {prev_knowledges.map((option) => (
                                        <MenuItem key={option.value} value={option.value}>
                                            {option.label}
                                        </MenuItem>
                                    ))}
                                </TextField>
                                : null}
                                </Grid>
                                

                                <br></br>
                                <br></br>
                                <Grid item xs={4}>
                                {profile ?
                                <TextField style={{maxWidth:"30vh", minWidth:"30vh"}}
                              
                                    id="standard-select-currency"
                                    select
                                    label="Extrovertiertheit"
                                    onChange={(event) => this.handleExtroversionChange(event.target.value)}
                                    defaultValue={profile.getExtroversion()}
                                    helperText="Bitte wählen sie ihre Extrovertiertheit"
                                >
                                    {extroversions.map((option) => (
                                        <MenuItem key={option.value} value={option.value}>
                                            {option.label}
                                        </MenuItem>
                                    ))}
                                </TextField>
                                
                                : null}
                                </Grid>
                                

                                <br></br>
                                <br></br>
                                <Grid item xs={4}>
                                {profile ?
                                <TextField style={{maxWidth:"30vh", minWidth:"30vh"}}
                              
                                    id="standard-select-currency"
                                    select
                                    label="Lernpräferenz"
                                    onChange={(event) => this.handleStudyStateChange(event.target.value)}
                                    defaultValue={profile.getStudyState()}
                                    helperText="Bitte wählen sie die Lernpräferenz"
                                >
                                    {studystates.map((option) => (
                                        <MenuItem key={option.value} value={option.value}>
                                            {option.label}
                                        </MenuItem>
                                    ))}
                                </TextField>
                                : null}
                                </Grid>
                            
                                <br></br>
                                <br></br>
                                <Grid item xs={4}>
                                {profile ?
                                <TextField style={{maxWidth:"30vh", minWidth:"30vh"}}
                              
                                    id="standard-select-currency"
                                    select
                                    label="Frequenz"
                                    onChange={(event) => this.handleFrequencyChange(event.target.value)}
                                    defaultValue={profile.getFrequency()}
                                    helperText="Bitte wählen sie die gewünschte Frequenz"
                                >
                                    {frequencys.map((option) => (
                                        <MenuItem key={option.value} value={option.value}>
                                            {option.label}
                                        </MenuItem>
                                    ))}
                                </TextField>
                                : null}
                                </Grid>

                                <br></br>
                                <br></br>
                                <Grid item xs={4}>
                                {profile ?
                                <TextField style={{maxWidth:"30vh", minWidth:"30vh"}}
                              
                                    id="standard-select-currency"
                                    select
                                    label="Lerntyp"
                                    onChange={(event) => this.handleLearntypChange(event.target.value)}
                                    defaultValue={profile.getLearntyp()}
                                    helperText="Bitte wählen sie ihren Lerntyp aus"
                                >
                                    {learntyps.map((option) => (
                                        <MenuItem key={option.value} value={option.value}>
                                            {option.label}
                                        </MenuItem>
                                    ))}
                                </TextField>
                                : null}
                                </Grid>

                                <br></br>
                                <br></br>
                                <Grid item xs={4}>
                                {profile ?
                                <TextField style={{maxWidth:"30vh", minWidth:"30vh"}}
                              
                                    id="standard-select-currency"
                                    select
                                    label="Semester"
                                    onChange={(event) => this.handleSemesterChange(event.target.value)}
                                    defaultValue={profile.getSemester()}
                                    helperText="Bitte wählen sie ihr Semester"
                                >
                                    {semesters.map((option) => (
                                        <MenuItem key={option.value} value={option.value}>
                                            {option.label}
                                        </MenuItem>
                                    ))}
                                </TextField>
                                : null}
                                </Grid>
                                <br></br>
                                <br></br>
                                <Grid item xs={12}>
                                <Button style={{maxWidth:"30vh", minWidth:"30vh", maxHeight:"5vh", minHeight:"5vh"}} variant="outlined" color="secondary" onClick={() => this.state.newProfileName != "" && this.state.newProfileName != null && this.state.newInterest != null && this.state.newInterest != "" && this.state.newDegreeCourse != null && this.state.newDegreeCourse != "" ? this.updateProfile() : null}>Speichern</Button>
                                </Grid>
                                </Grid>
                                <br></br>
                                
        <Divider />

            <br margin-top='20px' />

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
  paper: {
      backroundColer: 'orange'
  },
  content: {
    margin: theme.spacing(1),
  }
  
});

export default withStyles(styles)(UserProfile);