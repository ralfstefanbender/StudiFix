import React, { Component, useState } from "react";
import TableRow from '@material-ui/core/TableRow';
import TableCell from '@material-ui/core/TableCell';
import { Button } from '@material-ui/core';
import GroupInvitationBO from '../../api/GroupInvitationBO';
import StudyFixAPI from '../../api/StudyFixAPI';

class MatchingPageRow extends Component{
    constructor(props){
        super(props)
        this.state = {
            disabled:false
        }

    }

    handleGroupInvite = (e, match_id) =>{
        var newInvite = new GroupInvitationBO()
        newInvite.setSourceOwner(this.props.user_id)
        newInvite.setIsAccepted(false)
        newInvite.setTargetOwner(this.props.user_id)
        newInvite.setStudyGroupId(match_id)
        StudyFixAPI.getAPI().addGroupInvitation(newInvite).then(() => {this.setState({disabled:true})})

      }


    render(){
        const match = this.props.match

        return(
            <TableRow key={match.name}>
                <TableCell align="left">{match.name}</TableCell>
                <TableCell align="center">{match.semester}</TableCell>
                <TableCell align="center">{match.interest}</TableCell>
                <TableCell align="center"><b>{match.matching_score}</b></TableCell>
                <TableCell align="center">
                    <Button disabled={this.state.disabled} variant="contained" color="primary" onClick={(e)=>{this.handleGroupInvite(e, match.id)}}>
                    Anfrage senden
                    </Button>
                </TableCell>
            </TableRow>
        )
    }
}
export default MatchingPageRow