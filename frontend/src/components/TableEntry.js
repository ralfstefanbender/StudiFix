import React, { Component } from 'react';
import { Grid, Button } from "@material-ui/core";
import { StudyFixAPI } from '../api';
import {withStyles} from '@material-ui/core';
import DeleteIcon from '@material-ui/icons/Delete';
import LoadingProgress from '../components/dialogs/LoadingProgress';


class TableEntry extends Component {
    constructor(props) {
        super(props)
        this.state = {
            tableData: [],
            studygroups: [],
            studygroup: null,
            name: '',
            id: null,
            chat: null,
            error: null,
            updatingError: null,
            deletingError: null,
            loaded: false,
            loadingInProgress: false


        };
        this.baseState = this.state;
        this.toggleClass = this.toggleClass.bind(this);
        this.handleSelect = this.handleSelect.bind(this);
        this.handleChange = this.handleChange.bind(this);
    }

    componentDidMount(){
        this.getAllStudyGroups();
    }



     getAllStudyGroups = () => {
        StudyFixAPI.getAPI().getAllStudyGroups(this.props.studygroup)
        .then(studygroupBOs =>
            this.setState({
               studygroups: studygroupBOs,
               name: studygroupBOs.getName(),
               chat: studygroupBOs.getChatId(),
               id: studygroupBOs.getId(),
               error: null
            })).catch(e =>
                this.setState({
                    studygroups:[],
                    error: e
                }))
    }


    toggleClass(index, e) {
        this.setState({
          activeIndex: this.state.activeIndex === index ? null : index
        });
      }

    moreLess(index) {
        if (this.state.activeIndex === index) {
          return (
            <span>
              <i className="fas fa-angle-up" /> Hide Description
            </span>
          );
        } else {
          return (
            <span>
              <i className="fas fa-angle-down" /> Show Description
            </span>
          );
        }
      }

    handleSelect(){
        this.setState({select: !this.state.select})

    }

    handleChange(e) {
        this.setState({ priority: e.target.value });
      }






    render() {


        const { classes } = this.props;
        const {activeIndex, buttonText, loadingInProgress} = this.state;

        return (

            <Grid container justify="flex-start"  xs={12} xl={12} >
                 <Grid container justify="flex-start"  xs={12}>

                    <Grid item xs={3} md={3}>
                        {this.state.loaded ? this.state.name: null}
                    </Grid>
                     <Grid item xs={3} md={3}>
                        {this.state.loaded ? this.state.chat: null}
                    </Grid>
                    <Grid item xs={3} md={3}>
                        {this.state.loaded ? this.state.id: null}
                    </Grid>
                    <Grid item xs={3} md={3}>
                        <Button aria-label="delete"  variant="outlined">
                          <DeleteIcon fontSize="small" onClick={() => this.props.deleteStudyGroup(this.props.studygroup.getID())}/>
                        </Button>
                    </Grid>
                    </Grid>
                    <LoadingProgress show={loadingInProgress} />
                    </Grid>
        )
    }
}


const styles = theme => ({
    grid: {
        width: '100%',
        margin: '0px',
        paddingTop: theme.spacing(1)
    },
    button: {
        marginTop: theme.spacing(3)
    },
    redHeader: {
        color: theme.palette.red,
        fontFamily: 'Arial',
        fontStyle: 'bold',
        fontSize: 20
    },
    grayHeader: {
        color: theme.palette.gray,
        fontFamily: 'Arial',
        fontStyle: 'bold',
        fontSize: 35
    },


});
export default withStyles(styles) (TableEntry);