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

function Matching_page(currentUser) {
  const [matches, setmatches] = useState(null);
  const classes = useStyles();
  console.log(currentUser)
  return (
    <ThemeProvider theme={theme}>
      <Paper elevation={0} className={classes.root}>
        <div className={classes.content}>
          <Typography variant='h6'>
            Matching Algorithmus
        </Typography>
          <br />
          <Typography>
          <Button variant="contained" color="primary" onClick={()=>StudyFixAPI.getAPI().getMatchesUser(currentUser.currentUser.uid).then(UserMatchBO => setmatches(UserMatchBO))}>
          Matches Suchen
          </Button>
          
          <Table>
            <TableHead>
              <TableRow>
                <TableCell align="left">Name</TableCell>
                <TableCell align="center">Semester</TableCell>
                <TableCell align="center">Interests</TableCell>
                <TableCell align="center">Matching Score</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {matches? matches.map((match)=>(
                <TableRow key={match.name}>
                <TableCell align="left">{match.name}</TableCell>
                <TableCell align="center">{match.semester}</TableCell>
                <TableCell align="center">{match.interest}</TableCell>
                <TableCell align="center">{match.matching_score}</TableCell>
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