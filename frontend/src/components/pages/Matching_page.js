import React, { useState } from 'react'
import { makeStyles, Paper, Typography, Link } from '@material-ui/core';
import { ThemeProvider } from "@material-ui/core";
import theme from "../../theme";
import { Button } from '@material-ui/core';
import StudyFixAPI from '../../api/StudyFixAPI';

import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import ChatInvitationBO from '../../api/ChatInvitationBO';



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

function chatInvitation(targetId){
  var newInvite = new ChatInvitationBO()
  newInvite.setSourceOwner(1)
  newInvite.setIsAccepted(false)
  newInvite.setTargetOwner(targetId)
  newInvite.setChatId(1)
  return newInvite
} 

function Matching_page(currentUser) {
  const [matches, setmatches] = useState(null);
  const [group_matches, setgroup_matches] = useState(null);
  const sourceUser = ()=>{StudyFixAPI.getAPI().getUserByGoogleIdURL(currentUser.currentUser.uid)}
  const classes = useStyles();
  return (
    <ThemeProvider theme={theme}>
      <Paper elevation={0} className={classes.root}>
        <div className={classes.content}>
          
          <br />
          <Typography>
            <div align="center">
              <Typography variant='h8'>
                Mit einem Klick nach passenden Matches suchen  <br />
              </Typography>
            <Button align="center" variant="contained" color="primary" onClick={()=>{StudyFixAPI.getAPI().getMatchesUser(currentUser.currentUser.uid).then(UserMatchBO => setmatches(UserMatchBO)); StudyFixAPI.getAPI().getMatchesGroup(currentUser.currentUser.uid).then(GroupMatchBO => setgroup_matches(GroupMatchBO))}}>
              Matches Suchen
            </Button>
            <Button onClick={()=>{console.log(sourceUser)}}>
              test
            </Button>
            </div>
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
              {matches? matches.map((match)=>(
                <TableRow key={match.name}>
                <TableCell align="left">{match.name}</TableCell>
                <TableCell align="center">{match.semester}</TableCell>
                <TableCell align="center">{match.interest}</TableCell>
                <TableCell align="center"><b>{match.matching_score}</b></TableCell>
                <TableCell align="center">
                <Button disabled={false} variant="contained" color="primary" onClick={()=>{StudyFixAPI.getAPI().addChatInvitation(chatInvitation(match.id))}}>
                  Anfrage senden
                </Button>
                </TableCell>
              </TableRow>
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
              {group_matches? group_matches.map((match)=>(
                <TableRow key={match.name}>
                <TableCell align="left">{match.name}</TableCell>
                <TableCell align="center">{match.semester}</TableCell>
                <TableCell align="center">{match.interest}</TableCell>
                <TableCell align="center"><b>{match.matching_score}</b></TableCell>
                <TableCell align="center">
                <Button variant="contained" color="primary">
                  Anfrage senden
                </Button>
                </TableCell>
              </TableRow>
              )):null}
            </TableBody>
            
          </Table>
          </Typography>
        </div>
      </Paper>
    </ThemeProvider>
  )
}

export default Matching_page;