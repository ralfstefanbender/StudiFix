import React, { Component } from 'react';
import Grid from '@material-ui/core/Grid';
import {Typography} from '@material-ui/core';
import Container from '@material-ui/core/Container';
import {withStyles} from '@material-ui/core';
import { StudyFixAPI, StudyGroupBO } from '../api';
import TableEntry from './TableEntry';
import LoadingProgress from '../components/dialogs/LoadingProgress';




/**
 * Controlls  the list of archived projects.
 *
 * @see See [TableEntryButtonAdmin]
 *
 * @author [Gruppe]
 */
class StudyGroupListEntry extends Component {
constructor(props) {
        super(props)
        this.state = {
            tableData: [],
            studygroups: [],
            error: null,
            updatingError: null,
            deletingError: null,
            loaded: null,
            activeIndex: null,
            loadingInProgress: false



        };
        this.baseState = this.state;



    }
    componentDidMount(){
        this.getAllStudyGroups();
    }



     getAllStudyGroups = () => {
        StudyFixAPI.getAPI().getAllStudyGroups()
        .then(studygroupBOs =>
            this.setState({
               studygroups: studygroupBOs,
               error: null
            })).catch(e =>
                this.setState({
                    studygroups:[],
                    error: e
                }))
    }





  deleteStudyGroupHandler = (studygroupid) => {
        StudyFixAPI.getAPI().deleteStudyGroup(studygroupid)
        this.setState({
          studygroups: this.state.studygroups.filter(studygroupFromState => studygroupFromState.getID() != studygroupid)
        })
    }

  render() {
    const {studygroups, loadingInProgress} = this.state;
     const {classes}= this.props;
        return (

            <div>
             <Container maxWidth="md">
                <Grid container  justify="flex-start"  xs={12} className={classes.grid}>
                    <Grid item align="flex-start"  xs={12}>
                        <Typography color="secondary" variant='h4' className={classes.redHeader}> Alle Lerngruppen</Typography>
                    </Grid>
                            <Grid container justify="flex-start"  xs={12} className={classes.grid} spacing={2}>
                                    <Grid item align="center" xs={3} md={3}>
                                            <Typography variant="h6" className={classes.tableRow}>
                                                Lerngruppe
                                            </Typography>
                                    </Grid>
                                      <Grid item xs={3} md={3}>
                                            <Typography variant="h6" className={classes.tableRow}>
                                               Chat
                                            </Typography>
                                    </Grid>
                                    <Grid item xs={3} md={3}>
                                            <Typography variant="h6" className={classes.tableRow}>
                                                Id
                                            </Typography>
                                    </Grid>

                                    <Grid item xs={12} className={classes.grid}>
                                {this.state.studygroups.map(studygroup => (
                                            <TableEntry
                                                name = {studygroup.getName()}
                                                chat = {studygroup.getChatId()}
                                                id = {studygroup.getID()}
                                                deleteStudyGroup={this.deleteStudyGroupHandler}
                                            />
                                ))}
                                </Grid>
                    </Grid>
                    </Grid>
                    <LoadingProgress show={loadingInProgress} />
             </Container>
		    </div>
		);
  }
}

const styles = theme => ({
    grid:{
        width: '100%',
        margin: '0px',
        paddingTop: theme.spacing(3)
    },
    button:{
        marginTop: theme.spacing(3)
    },
    redHeader:{
        color: theme.palette.red,
        fontFamily: 'Arial',
        fontStyle: 'bold',
        fontSize: 30
    },
    tableRow:{
    color:'lightGray',
    fontFamily:'Arial'
    }
});
export default withStyles(styles) (StudyGroupListEntry);