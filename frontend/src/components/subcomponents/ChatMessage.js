import { Button, Card} from '@material-ui/core'
import React, { Component } from 'react'


class ChatMessage extends Component {
    constructor(props){
        super(props)

        this.state = {
            user: this.props.user[0],
            currUser: this.props.currUser,
            chatMessage: this.props.chatMessage,
            style:{width:"fit-content", paddingLeft:"1vw", paddingRight:"1vw", textAlign:"right", minWidth:"8vw"},
            divStyle: {alignSelf:"flex-end"},
            unknownUser: "Unknown User"
        }
    }

    componentDidMount(){
        if(this.state.user == this.state.currUser){this.setState({style:{backgroundColor:"#90EE90",minWidth:"8vw", width:"fit-content", paddingLeft:"1vw", paddingRight:"1vw"}, divStyle:{}})}
    }
        
    

    render() {
        
        return (
            <div style={this.state.divStyle}>
                <Card variant='outlined' style={this.state.style}> {this.state.user?<b>{this.state.user.firstname}</b>: <b>{this.state.unknownUser}</b>} <br/> {this.state.chatMessage.text}</Card> {this.state.chatMessage.creation_date.slice(0, 10)}
                {this.state.chatMessage.id != 0?<Button size="small" onClick={() => this.props.deleteChatMessage(this.state.chatMessage.id)}>x</Button>:null}
            </div>
        )
    }
}

export default ChatMessage