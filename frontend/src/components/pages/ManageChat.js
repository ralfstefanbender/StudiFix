import React, { Component } from 'react'
import ChatWindow from '../subcomponents/ChatWindow'
import ChatSelection from '../subcomponents/ChatSelection'
import { StudyFixAPI } from '../../api'
import GroupChatSelection from "../subcomponents/GroupChatSelection"
import {Card, Typography} from "@material-ui/core";
import firebase from 'firebase/app';

class ManageChat extends Component {

  constructor(props){
    super(props)

    this.state = {
      currentUser: null,
      chats:null,
      groupchats:null,
      selectedChat: null,
      selectedGroupChat:null,
    }
  }

  componentDidMount(){
    this.getCurrentUser()
  }

  getCurrentUser(){
    StudyFixAPI.getAPI().getUserByGoogleId(firebase.auth().currentUser.uid).then((user) => {this.setState({currentUser:user}); this.getAllChats(user.id)})
  }

  getAllChats(id){
    StudyFixAPI.getAPI().getChatByUserId(id).then((chats) => {this.setState({chats:chats})})
    StudyFixAPI.getAPI().getGroupChatByUserId(id).then((groupchats) => (this.setState({groupchats:groupchats})))
  }

  getAllGroupChats(id){
    StudyFixAPI.getAPI().getGroupChatByUserId(id).then((groupchats) => (this.setState({chats:groupchats})))
  }
  setSelectedChat = (selChat) =>{
    this.setState({selectedChat:selChat})
  }


  render(){
  return (
    <>
      <div className="Container" style={{display:"grid", gridTemplateColumns:"30% 70%"}}>
        <div>
        {this.state.chats? <ChatSelection chats={this.state.chats}  setSelectedChat={this.setSelectedChat}/>:null}
        {this.state.groupchats? <GroupChatSelection groupchats={this.state.groupchats} setSelectedChat={this.setSelectedChat}/>:null}
        </div>
        {this.state.selectedChat == null &&
          <Card variant='outlined'>
                <Card variant='outlined'>
                <Typography variant='h6' color ="primary" fontFamily = "-apple-system" align='center'>
                  &#10094;&#10094;&nbsp; Wähle hier deinen Chat aus!</Typography>
                </Card>
          </Card>
          }
        {this.state.selectedChat && this.state.currentUser? <ChatWindow key={this.state.selectedChat.id} chat={this.state.selectedChat} currentUser={this.state.currentUser}/>:null}
      </div>
    </>
  )}
}

export default ManageChat