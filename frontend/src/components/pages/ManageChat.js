import React, { Component } from 'react'
import ChatWindow from '../subcomponents/ChatWindow'
import ChatSelection from '../subcomponents/ChatSelection'
import { StudyFixAPI } from '../../api'

class ManageChat extends Component {

  constructor(props){
    super(props)

    this.state = {
      currentUser: null,
      chats:null,
      selectedChat: null,
    }
  }

  componentDidMount(){
    this.getCurrentUser()
  }

  getCurrentUser(){
    StudyFixAPI.getAPI().getUserByGoogleId(this.props.currentUser.uid).then((user) => {this.setState({currentUser:user}); this.getAllChats(user.id)})
  }

  getAllChats(id){
    StudyFixAPI.getAPI().getChatByUserId(id).then((chats) => (this.setState({chats:chats})))
  }

  setSelectedChat = (selChat) =>{
    this.setState({selectedChat:selChat})
  }

  render(){
  return (
    <>
      <div className="Container" style={{display:"grid", gridTemplateColumns:"30% 70%"}}>
        {this.state.chats?<ChatSelection chats={this.state.chats} setSelectedChat={this.setSelectedChat}/>:null}
        {this.state.selectedChat? <ChatWindow key={this.state.selectedChat.id} chat={this.state.selectedChat} currentUser={this.state.currentUser}/>:null}
      </div>
    </>
  )}
}

export default ManageChat