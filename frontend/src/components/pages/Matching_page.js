import React from 'react'
import { makeStyles, Paper, Typography, Link } from '@material-ui/core';
import { ThemeProvider } from "@material-ui/core";
import theme from "../../theme";

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

function Matching_page() {

  const classes = useStyles();

  return (
    <ThemeProvider theme={theme}>
      <Paper elevation={0} className={classes.root}>
        <div className={classes.content}>
          <Typography variant='h6'>
            Matching Algorithmus
        </Typography>
          <br />
          <Typography>
            <h4>Test Test</h4>
          </Typography>

        </Typography>
        </div>
      </Paper>
    </ThemeProvider>
  )
}

export default About;