import React from 'react'
import { makeStyles, Paper, Typography, Link } from '@material-ui/core';

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


function ManageStudyGroup() {

  const classes = useStyles();

  return (
    <Paper elevation={0} className={classes.root}>
      <div className={classes.content}>
        <Typography variant='h6'>
          Lerngruppen
        </Typography>

      </div>
    </Paper>
  )
}

export default ManageStudyGroup;