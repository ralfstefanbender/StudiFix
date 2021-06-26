import React, { Component } from 'react'
import { makeStyles, withStyles, Paper, Typography, Link } from '@material-ui/core';
import { ThemeProvider } from "@material-ui/core";
import theme from "../../theme";
import { Button } from '@material-ui/core';
import StudyFixAPI from '../../api/StudyFixAPI';

import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';


import MatchingPageRow from '../subcomponents/MatchingPageRow';
import MatchingPageRowGroups from '../subcomponents/MatchingPageRowGroups'

class Matching_page extends Component {

  constructor(props){
    super(props);
    this.state={
      current_user:null,
      matches:null,
      group_matches:null
    }
  }

  componentDidMount(){
    this.getCurrentUser()
  }

  getCurrentUser(){
    StudyFixAPI.getAPI().getUserByGoogleId(this.props.currentUser.uid).then((user) => {this.setState({current_user:user})})
  }

  handleMatchSearch(){
    StudyFixAPI.getAPI().getMatchesUser(this.state.current_user.getGoogleId()).then(UserMatchBO => this.setState({matches:UserMatchBO})); 
    StudyFixAPI.getAPI().getMatchesGroup(this.state.current_user.getGoogleId()).then(GroupMatchBO => this.setState({group_matches:GroupMatchBO}))
  }



  render(){

    const { classes } = this.props;

    return (
      <ThemeProvider theme={theme}>
        <Paper elevation={0} className={classes.root}>
          <div className={classes.content}>
            
            <br />
            <Typography>
              <bruh align="center">
                <Typography variant='h8'>
                  Mit einem Klick nach passenden Matches suchen  <br />
                </Typography>
              <Button align="center" variant="contained" color="secondary" onClick={()=>{this.handleMatchSearch()}}>
                Matches Suchen
              </Button>
              </bruh>
            <Typography variant='h6'>
              User Matches
            </Typography>
            <Table>
              <TableHead>
                <TableRow>
                  <TableCell align="left"><b>Name</b></TableCell>
                  <TableCell align="center"><b>Semester</b></TableCell>
                  <TableCell align="center"><b>Interests</b></TableCell>
                  <TableCell align="center"><b>Matching Score</b></TableCell>
                  <TableCell align="center"></TableCell>
                </TableRow>
              </TableHead>
              <TableBody>
                {this.state.matches? this.state.matches.map((match)=>(
                  <MatchingPageRow key={match.id} match={match} user_id={this.state.current_user.id}>  
                  </MatchingPageRow>
                )):null}
              </TableBody>
              
            </Table>
            <Typography variant='h6'>
            <br />Gruppen Matches
            </Typography>
            <Table>
              <TableHead>
                <TableRow>
                  <TableCell align="left"><b>Name</b></TableCell>
                  <TableCell align="center"><b>Prefered Semester</b></TableCell>
                  <TableCell align="center"><b>Interests</b></TableCell>
                  <TableCell align="center"><b>Matching Score</b></TableCell>
                  <TableCell align="center"></TableCell>
                </TableRow>
              </TableHead>
              <TableBody>
                {this.state.group_matches? this.state.group_matches.map((group_matches)=>(
                  <MatchingPageRowGroups key={group_matches.id} match={group_matches} user_id={this.state.current_user.id}>
                  </MatchingPageRowGroups>
                )):null}
              </TableBody>
              
            </Table>
            </Typography>
          </div>
        </Paper>
      </ThemeProvider>
    )
  }
}

const useStyles = makeStyles(theme => ({
  root: {
    width: '100%',
    marginTop: theme.spacing(2),
    marginBottom: theme.spacing(2),
    padding: theme.spacing(1)
  },
  content: {
    margin: theme.spacing(1),
  }
}));

export default withStyles(useStyles)(Matching_page);