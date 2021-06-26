import ChatBO from './ChatBO';
import ChatInvitationBO from './ChatInvitationBO';
import ChatMessageBO from './ChatMessageBO';
import GroupInvitationBO from './GroupInvitationBO';
import LearningProfileUserBO from './LearningProfileUserBO';
import LearningProfileGroupBO from './LearningProfileGroupBO';
import StudyGroupBO from './StudyGroupBO';
import UserBO from './UserBO';
import UserMatchBO from './UserMatchBO';
import GroupMatchBO from './GroupMatchBO';


export default class StudyFixAPI {

     // Singelton instance
    static #api = null;

    // Local Python backend
    #studyfixServerBaseURL ='/studyfix';

    //Chatinvitation related
    #getAllChatInvitationsURL = () => `${this.#studyfixServerBaseURL}/chatinvitation`;
    #getChatInvitationURL = (id) => `${this.#studyfixServerBaseURL}/chatinvitation/${id}`;
    #addChatInvitationURL = () => `${this.#studyfixServerBaseURL}/chatinvitation`;
    #deleteChatInvitationURL = (id) => `${this.#studyfixServerBaseURL}/chatinvitation/${id}`;
    #updateChatInvitationURL = (id) => `${this.#studyfixServerBaseURL}/chatinvitation/${id}`;
    #getChatInvitationByTargetUserURL = (target_user) => `${this.#studyfixServerBaseURL}/chatinvitation-by-target-user/${target_user}`;
    #getChatInvitationBySourceUserURL = (source_user) => `${this.#studyfixServerBaseURL}/chatinvitation-by-target-user/${source_user}`;
    #getChatInvitationByChatURL = (chat_id) => `${this.#studyfixServerBaseURL}/chatinvitation-by-chat/${chat_id}`;
    #getChatInvitationPendInvitesURL = () => `${this.#studyfixServerBaseURL}/chatinvitation-pend-invites`;
    #getChatInvitationPendInvitesTargetURL = (target_user) => `${this.#studyfixServerBaseURL}/chatinvitation-pend-invites-target/${target_user}`;
    #getChatInvitationPendInvitesSourceURL = (source_user) => `${this.#studyfixServerBaseURL}/chatinvitation-pend-invites-source/${source_user}`;
    #getChatInvitationAcceptedInvitesSourceURL = (source_user) => `${this.#studyfixServerBaseURL}/chatinvitation-accepted-invites-source/${source_user}`;
    #getChatInvitationAcceptedInvitesTargetURL = (target_user) => `${this.#studyfixServerBaseURL}/chatinvitation-accepted-invites-target/${target_user}`;

    //GroupInvitation
    #getAllGroupInvitationsURL = () => `${this.#studyfixServerBaseURL}/groupinvitation`;
    #getGroupInvitationURL = (id) => `${this.#studyfixServerBaseURL}/groupinvitation/${id}`;
    #addGroupInvitationURL = () => `${this.#studyfixServerBaseURL}/groupinvitation`;
    #deleteGroupInvitationURL = (id) => `${this.#studyfixServerBaseURL}/groupinvitation/${id}`;
    #updateGroupInvitationURL = (id) => `${this.#studyfixServerBaseURL}/groupinvitation/${id}`;
    #getGroupInvitationByStudyGroupURL = (study_group_id) => `${this.#studyfixServerBaseURL}/groupinvitation-by-study-group/${study_group_id}`;
    #getGroupInvitationByTargetUserURL = (target_user) => `${this.#studyfixServerBaseURL}/groupinvitation-by-target-user/${target_user}`;
    #getGroupInvitationBySourceUserURL = (source_user) => `${this.#studyfixServerBaseURL}/groupinvitation-by-source-user/${source_user}`;
    #getGroupInvitationPendInvitesURL = () => `${this.#studyfixServerBaseURL}/groupinvitation-pend-invites`;
    #getGroupInvitationAcceptedByStudyGroupURL = (study_group_id) => `${this.#studyfixServerBaseURL}/groupinvitation-accepted-by-study-group/${study_group_id}`;
    #getGroupInvitationPendInvitesTargetURL = (target_user) => `${this.#studyfixServerBaseURL}/groupinvitation-pend-invites-target/${target_user}`;
    #getGroupInvitationPendInvitesSourceURL = (source_user) => `${this.#studyfixServerBaseURL}/groupinvitation-pend-invites-source/${source_user}`;
    #getGroupInvitationAcceptedInvitesSourceURL = (source_user) => `${this.#studyfixServerBaseURL}/groupinvitation-accepted-invites-source/${source_user}`;
    #getGroupInvitationAcceptedInvitesTargetURL = (target_user) => `${this.#studyfixServerBaseURL}/groupinvitation-accepted-invites-target/${target_user}`;

    //User
    #getAllUsersURL = () => `${this.#studyfixServerBaseURL}/user`;
    #getUserByIdURL = (id) => `${this.#studyfixServerBaseURL}/user/${id}`;
    #addUserURL = () => `${this.#studyfixServerBaseURL}/user`;
    #deleteUserURL = (id) => `${this.#studyfixServerBaseURL}/user/${id}`;
    #updateUserURL = (id) => `${this.#studyfixServerBaseURL}/user/${id}`;
    #getUserByLastnameURL = (lastname) => `${this.#studyfixServerBaseURL}/user-by-lastname/${lastname}`;
    #getUserByFirstnameURL = (firstname) => `${this.#studyfixServerBaseURL}/user-by-firstname/${firstname}`;
    #getUserByMailURL = (email) => `${this.#studyfixServerBaseURL}/user-by-mail/${email}`;
    #getUserByGoogleIdURL = (google_id) => `${this.#studyfixServerBaseURL}/user-by-google-id/${google_id}`;


    //Studygroup
    #getAllStudyGroupsURL = () => `${this.#studyfixServerBaseURL}/studygroup`;
    #getStudyGroupByIdURL = (id) => `${this.#studyfixServerBaseURL}/studygroup/${id}`;
    #addStudyGroupURL = () => `${this.#studyfixServerBaseURL}/studygroup`;
    #deleteStudyGroupURL = (id) => `${this.#studyfixServerBaseURL}/studygroup/${id}`;
    #updateStudyGroupURL = (id) => `${this.#studyfixServerBaseURL}/studygroup/${id}`;
    #getStudyGroupByNameURL = (name) => `${this.#studyfixServerBaseURL}/studygroup/${name}`;
    #getUserPendingGroupInvites = (id) => `${this.#studyfixServerBaseURL}/pending_group_invites-by-google-id/${id}`;
    #createStudyGroupPackage = (name, user_id) => `${this.#studyfixServerBaseURL}/create-study-group-package/${name}/${user_id}`;

    //LearningProfileGroup
    #getAllLearningProfileGroupsURL = () => `${this.#studyfixServerBaseURL}/learningprofilegroup`;
    #getLearningProfileGroupByIdURL = (id) => `${this.#studyfixServerBaseURL}/learningprofilegroup/${id}`;
    #addLearningProfileGroupURL = () => `${this.#studyfixServerBaseURL}/learningprofilegroup`;
    #deleteLearningProfileGroupURL = (id) => `${this.#studyfixServerBaseURL}/learningprofilegroup/${id}`;
    #updateLearningProfileGroupURL = (id) => `${this.#studyfixServerBaseURL}/learningprofilegroup/${id}`;
    #getLearningProfileGroupByNameURL = (name) => `${this.#studyfixServerBaseURL}/learningprofilegroup-by-name/${name}`;

    //LearningProfileUser
    #getAllLearningProfileUsersURL = () => `${this.#studyfixServerBaseURL}/learningprofileuser`;
    #getLearningProfileUserByIdURL = (id) => `${this.#studyfixServerBaseURL}/learningprofileuser/${id}`;
    #getLearningProfileUserByUserIdURL = (id) => `${this.#studyfixServerBaseURL}/learningprofileuser-by-user-id/${id}`;
    #addLearningProfileUserURL = () => `${this.#studyfixServerBaseURL}/learningprofileuser`;
    #deleteLearningProfileUserURL = (id) => `${this.#studyfixServerBaseURL}/learningprofileuser/${id}`;
    #updateLearningProfileUserURL = (id) => `${this.#studyfixServerBaseURL}/learningprofileuser/${id}`;
    #getLearningProfileUserByNameURL = (name) => `${this.#studyfixServerBaseURL}/learningprofileuser-by-name/${name}`;

    //Chatmessage
    #getAllChatMessagesURL = () => `${this.#studyfixServerBaseURL}/chatmessage`;
    #getChatMessageByIdURL = (id) => `${this.#studyfixServerBaseURL}/chatmessage/${id}`;
    #addChatMessageURL = () => `${this.#studyfixServerBaseURL}/chatmessage`;
    #deleteChatMessageURL = (id) => `${this.#studyfixServerBaseURL}/chatmessage/${id}`;
    #updateChatMessageURL = (id) => `${this.#studyfixServerBaseURL}/chatmessage/${id}`;
    #getChatMessageByChatIdURL = (chat_id) => `${this.#studyfixServerBaseURL}/chatmessage-chat-id/${chat_id}`;


    //Chat
    #getAllChatsURL = () => `${this.#studyfixServerBaseURL}/chat`;
    #getChatByIdURL = (id) => `${this.#studyfixServerBaseURL}/chat/${id}`;
    #getChatByUserId = (id) => `${this.#studyfixServerBaseURL}/chat-by-user-id/${id}`;
    #addChatURL = () => `${this.#studyfixServerBaseURL}/chat`;
    #getOtherUserByChatId = (current_user, chat_id) => `${this.#studyfixServerBaseURL}/other-user-by-chat-id/${current_user}/${chat_id}`;
    #deleteChatURL = (id) => `${this.#studyfixServerBaseURL}/chat/${id}`;
    #updateChatURL = (id) => `${this.#studyfixServerBaseURL}/chat/${id}`;

    //Matching
    #getMatches = (id) => `${this.#studyfixServerBaseURL}/matching/${id}`;
    #getGroupMatches = (id) => `${this.#studyfixServerBaseURL}/groupmatching/${id}`;
    #getAuth = () => `${this.#studyfixServerBaseURL}/auth`;
    #getFriendsByGoogleId = (id) => `${this.#studyfixServerBaseURL}/friends-by-google-id/${id}`;
    #getFriendRequestsByGoogleId = (id) => `${this.#studyfixServerBaseURL}/friend-requests-by-google-id/${id}`;
    #getGroupsByGoogleId = (id) => `${this.#studyfixServerBaseURL}/groups-by-google-id/${id}`;
    #acceptFriendRequest = (target_id, source_id) => `${this.#studyfixServerBaseURL}/acceptfriendrequests/${target_id}/${source_id}`;
    #declineFriendRequest = (target_id, source_id) => `${this.#studyfixServerBaseURL}/declinefriendrequests/${target_id}/${source_id}`;
    #removeFriend = (target_id, source_id) => `${this.#studyfixServerBaseURL}/removefriend/${target_id}/${source_id}`;
    #leaveGroup = (target_id, group_id) => `${this.#studyfixServerBaseURL}/leavegroup/${target_id}/${group_id}`;

    /**
   * Get the Singelton instance
   *
   * @public
   */
    static getAPI() {
        if (this.#api == null) {
          this.#api = new StudyFixAPI();
        }
        return this.#api;
      }

  /**
   *  Returns a Promise which resolves to a json object.
   *  The Promise returned from fetch() won’t reject on HTTP error status even if the response is an HTTP 404 or 500.
   *  fetchAdvanced throws an Error also an server status errors
   */
    #fetchAdvanced = (url, init) => fetch(url, init)
    .then(res => {
      // The Promise returned from fetch() won’t reject on HTTP error status even if the response is an HTTP 404 or 500.
      if (!res.ok) {
        throw Error(`${res.status} ${res.statusText}`);
      }
      return res.json();
    }
    )

 //Chatmessage
     /**
   * Returns a Promise, which resolves to an Array of ChatMessageBOs
   *
   * @public
   */
    getAllChatmessages(){
        return this.#fetchAdvanced(this.#getAllChatMessagesURL()).then((responseJSON) => {
            let chatmessageBOs = ChatMessageBO.fromJSON(responseJSON);
            return new Promise(function (resolve){
                resolve(chatmessageBOs)
            })
        })
    }

    /**
    *@param {Number} chatmessageID
    *@public
    */
    getChatMessageById(chatmessageID){
        return this.#fetchAdvanced(this.#getChatMessageByIdURL(chatmessageID)).then((responseJSON) => {
            let responseChatMessageBO = ChatMessageBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
              resolve(responseChatMessageBO);
            })
          })
    }

      /**
   * Adds a chatmessage and returns a Promise, which resolves to a new chatmessageBO object
   *
   * @param {chatmessageBO} chatmessageBO to be added. The ID of the new chat is set by the backend
   * @public

   */
    addChatMessage(chatmessageBO){
        return this.#fetchAdvanced(this.#addChatMessageURL(), {
          method: 'POST',
          headers:{
            'Accept': 'application/json, text/plain',
            'Content-type': 'application/json',
          },
          body: JSON.stringify(chatmessageBO)
            }).then((responseJSON) => {
            let responseChatMessageBO = ChatMessageBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
              resolve(responseChatMessageBO);
            })
          })
    }

       /**
   * Returns a Promise, which resolves to an Array of ChatmessageBOs
   * @param {ChatmessageID} ChatmessageBO to be deleted
   * @public
   */
    deleteChatMessage(chatmessageID){
        return this.#fetchAdvanced(this.#deleteChatMessageURL(chatmessageID), {
            method: 'DELETE'
          }).then((responseJSON) => {
            let responseChatMessageBO = ChatMessageBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
              resolve(responseChatMessageBO);
            })
          })
    }

   /**
   * Updates a Chatmessage and returns a Promise, which resolves to a  ChatmessageBO.
   * @param {ChatmessageBO} ChatmessageBO to be updated
   * @public
   */
    updateChatMessage(chatmessage){
        return this.#fetchAdvanced(this.#updateChatMessageURL(chatmessage.getID()), {
            method: 'PUT',
            headers:{
            'Accept': 'application/json, text/plain',
            'Content-type': 'application/json',
            },
            body: JSON.stringify(chatmessage)
          }).then((responseJSON) => {
            let responseChatMessageBO = ChatMessageBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
              resolve(responseChatMessageBO);
            })
          })
    }

    /**
    *@param {Number} chatmessage by Chat ID
    *@public
    */
    getChatMessageByChatId(chatID){
        return this.#fetchAdvanced(this.#getChatMessageByChatIdURL(chatID)).then((responseJSON) => {
            let responseChatMessageBO = ChatMessageBO.fromJSON(responseJSON);
            return new Promise(function (resolve) {
              resolve(responseChatMessageBO);
            })
          })
    }





 //Chat
     /**
   * Returns a Promise, which resolves to an Array of ChatBOs
   *
   * @public
   */
    getAllChats(){
        return this.#fetchAdvanced(this.#getAllChatsURL()).then((responseJSON) => {
            let chatBOs = ChatBO.fromJSON(responseJSON);
            return new Promise(function (resolve){
                resolve(chatBOs)
            })
        })
    }

    /**
    *@param {Number} chatID
    *@public
    */
    getChatById(chatID){
        return this.#fetchAdvanced(this.#getChatByIdURL(chatID)).then((responseJSON) => {
            let responseChatBO = ChatBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
              resolve(responseChatBO);
            })
          })
    }

      /**
   * Adds a chat and returns a Promise, which resolves to a new chatBO object
   *
   * @param {chatBO} chatBO to be added. The ID of the new chat is set by the backend
   * @public

   */
    addChat(chatBO){
        return this.#fetchAdvanced(this.#addChatURL(), {
          method: 'POST',
          headers:{
            'Accept': 'application/json, text/plain',
            'Content-type': 'application/json',
          },
          body: JSON.stringify(chatBO)
            }).then((responseJSON) => {
            let responseChatBO = ChatBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
              resolve(responseChatBO);
            })
          })
    }

       /**
   * Returns a Promise, which resolves to an Array of ChatBOs
   * @param {ChatID} ChatBO to be deleted
   * @public
   */
    deleteChat(chatID){
        return this.#fetchAdvanced(this.#deleteChatURL(chatID), {
            method: 'DELETE'
          }).then((responseJSON) => {
            let responseChatBO = ChatBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
              resolve(responseChatBO);
            })
          })
    }

   /**
   * Updates a Chat and returns a Promise, which resolves to a  ChatBO.
   * @param {ChatBO} ChatBO to be updated
   * @public
   */
    updateChat(chat){
        return this.#fetchAdvanced(this.#updateChatURL(chat.getID()), {
            method: 'PUT',
            headers:{
            'Accept': 'application/json, text/plain',
            'Content-type': 'application/json',
            },
            body: JSON.stringify(chat)
          }).then((responseJSON) => {
            let responseChatBO = ChatBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
              resolve(responseChatBO);
            })
          })
    }







 //Studygroup

     /**
   * Returns a Promise, which resolves to an Array of StudyGroupsBOs
   *
   * @public
   */
    getAllStudyGroups(){
        return this.#fetchAdvanced(this.#getAllStudyGroupsURL()).then((responseJSON) => {
            let studygroupBOs = StudyGroupBO.fromJSON(responseJSON);
            return new Promise(function (resolve){
                resolve(studygroupBOs)
            })
        })
    }

    /**
    *@param {Number} studygroupID
    *@public
    */
    getStudyGroupById(studygroupID){
        return this.#fetchAdvanced(this.#getStudyGroupByIdURL(studygroupID)).then((responseJSON) => {
            let responseStudyGroupBO = StudyGroupBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
              resolve(responseStudyGroupBO);
            })
          })
    }

      /**
   * Adds a user and returns a Promise, which resolves to a new studygroupBO object
   *
   * @param {studygroupBO} studygroupBO to be added. The ID of the new studygroup is set by the backend
   * @public

   */
    addStudyGroup(studygroupBO){
        return this.#fetchAdvanced(this.#addStudyGroupURL(), {
          method: 'POST',
          headers:{
            'Accept': 'application/json, text/plain',
            'Content-type': 'application/json',
          },
          body: JSON.stringify(studygroupBO)
            }).then((responseJSON) => {
            let responseStudyGroupBO = StudyGroupBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
              resolve(responseStudyGroupBO);
            })
          })
    }

       /**
   * Returns a Promise, which resolves to an Array of StudyGroupBOs
   * @param {StudyGroupID} StudyGroupBO to be deleted
   * @public
   */
    deleteStudyGroup(studygroupID){
        return this.#fetchAdvanced(this.#deleteStudyGroupURL(studygroupID), {
            method: 'DELETE'
          }).then((responseJSON) => {
            let responseStudyGroupBO = StudyGroupBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
              resolve(responseStudyGroupBO);
            })
          })
    }

   /**
   * Updates a StudyGroupGroup and returns a Promise, which resolves to a  StudyGroupBO.
   * @param {StudyGroupBO} StudyGroupBO to be updated
   * @public
   */
    updateStudyGroup(studygroup){
        return this.#fetchAdvanced(this.#updateStudyGroupURL(studygroup.getID()), {
            method: 'PUT',
            headers:{
            'Accept': 'application/json, text/plain',
            'Content-type': 'application/json',
            },
            body: JSON.stringify(studygroup)
          }).then((responseJSON) => {
            let responseStudyGroupBO = StudyGroupBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
              resolve(responseStudyGroupBO);
            })
          })
    }


      /**
   * Returns a Promise, which resolves to a StudyGroupBO
   * @param {name} name of the StudyGroup to be retrieved
   * @public
   */
    getStudyGroupByName(name){
      return this.#fetchAdvanced(this.#getStudyGroupByNameURL(name)).then((responseJSON) => {
        let StudyGroupBOs = StudyGroupBO.fromJSON(responseJSON)[0];
        return new Promise(function (resolve) {
          resolve(StudyGroupBOs);
      })
    })
    }

    createStudyGroupPackage(name, user_id){
        return this.#fetchAdvanced(this.#createStudyGroupPackage(name,user_id))
    }



  //Learningprofilegroup

     /**
   * Returns a Promise, which resolves to an Array of LearningProfileGroupsBOs
   *
   * @public
   */
    getAllLearningProfileGroups(){
        return this.#fetchAdvanced(this.#getAllLearningProfileGroupsURL()).then((responseJSON) => {
            let learningprofilegroupBOs = LearningProfileGroupBO.fromJSON(responseJSON);
            return new Promise(function (resolve){
                resolve(learningprofilegroupBOs)
            })
        })
    }

    /**
    *@param {Number} learningprofilegroupID
    *@public
    */
    getLearningProfileGroupById(learningprofilegroupID){
        return this.#fetchAdvanced(this.#getLearningProfileGroupByIdURL(learningprofilegroupID)).then((responseJSON) => {
            let responseLearningProfileGroupBO = LearningProfileGroupBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
              resolve(responseLearningProfileGroupBO);
            })
          })
    }

      /**
   * Adds a user and returns a Promise, which resolves to a new LearningProfileGroupBO object
   *
   * @param {learningprofilegroupBO} learningprofilegroupBO to be added. The ID of the new learningprofilegroup is set by the backend
   * @public

   */
    addLearningProfileGroup(learningprofilegroupBO){
        return this.#fetchAdvanced(this.#addLearningProfileGroupURL(), {
          method: 'POST',
          headers:{
            'Accept': 'application/json, text/plain',
            'Content-type': 'application/json',
          },
          body: JSON.stringify(learningprofilegroupBO)
            }).then((responseJSON) => {
            let responseLearningProfileGroupBO = LearningProfileGroupBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
              resolve(responseLearningProfileGroupBO);
            })
          })
    }

       /**
   * Returns a Promise, which resolves to an Array of LearningProfileGroupBOs
   * @param {LearningProfileGroupID} LearningProfileGroupBO to be deleted
   * @public
   */
    deleteLearningProfileGroup(learningprofilegroupID){
        return this.#fetchAdvanced(this.#deleteLearningProfileGroupURL(learningprofilegroupID), {
            method: 'DELETE'
          }).then((responseJSON) => {
            let responseLearningProfileGroupBO = LearningProfileGroupBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
              resolve(responseLearningProfileGroupBO);
            })
          })
    }

   /**
   * Updates a LearningProfileGroup and returns a Promise, which resolves to a  LearningProfileUserBO.
   * @param {learningprofileGroupBO}  LearningProfileGroupBO to be updated
   * @public
   */
    updateLearningProfileGroup(learningprofilegroup){
        return this.#fetchAdvanced(this.#updateLearningProfileGroupURL(learningprofilegroup.getID()), {
            method: 'PUT',
            headers:{
            'Accept': 'application/json, text/plain',
            'Content-type': 'application/json',
            },
            body: JSON.stringify(learningprofilegroup)
          }).then((responseJSON) => {
            let responseLearningProfileGroupBO = LearningProfileGroupBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
              resolve(responseLearningProfileGroupBO);
            })
          })
    }

  /**
   * Returns a Promise, which resolves to a LearningProfileGroupBO
   * @param {name} user name of the LearningProfileGroup to be retrieved
   * @public
   */
    getLearningProfileGroupByName(name){
      return this.#fetchAdvanced(this.#getLearningProfileGroupByNameURL(name)).then((responseJSON) => {
        let LearningProfileGroupBOs = LearningProfileGroupBO.fromJSON(responseJSON)[0];
        return new Promise(function (resolve) {
          resolve(LearningProfileGroupBOs);
      })
    })
    }









  //Learningprofileuser

     /**
   * Returns a Promise, which resolves to an Array of LearningProfileUsersBOs
   *
   * @public
   */
    getAllLearningProfileUsers(){
        return this.#fetchAdvanced(this.#getAllLearningProfileUsersURL()).then((responseJSON) => {
            let learningprofileuserBOs = LearningProfileUserBO.fromJSON(responseJSON);
            return new Promise(function (resolve){
                resolve(learningprofileuserBOs)
            })
        })
    }

    /**
    *@param {Number} learningprofileuserID
    *@public
    */
    getLearningProfileUserById(learningprofileuserID){
        return this.#fetchAdvanced(this.#getLearningProfileUserByIdURL(learningprofileuserID)).then((responseJSON) => {
            let responseLearningProfileUserBO = LearningProfileUserBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
              resolve(responseLearningProfileUserBO);
            })
          })
    }

    /**
    *@param {Number} learningprofileuserID
    *@public
    */
    getLearningProfileUserByUserId(learningprofileuserID){
      return this.#fetchAdvanced(this.#getLearningProfileUserByUserIdURL(learningprofileuserID)).then((responseJSON) => {
          let responseLearningProfileUserBO = LearningProfileUserBO.fromJSON(responseJSON)[0];
          return new Promise(function (resolve) {
            resolve(responseLearningProfileUserBO);
          })
        })
  }

      /**
   * Adds a user and returns a Promise, which resolves to a new UserBO object
   *
   * @param {learningprofileuserBO} learningprofileuserBO to be added. The ID of the new learningprofileuser is set by the backend
   * @public

   */
    addLearningProfileUser(learningprofileuserBO){
        return this.#fetchAdvanced(this.#addLearningProfileUserURL(), {
          method: 'POST',
          headers:{
            'Accept': 'application/json, text/plain',
            'Content-type': 'application/json',
          },
          body: JSON.stringify(learningprofileuserBO)
            }).then((responseJSON) => {
            let responseLearningProfileUserBO = LearningProfileUserBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
              resolve(responseLearningProfileUserBO);
            })
          })
    }

       /**
   * Returns a Promise, which resolves to an Array of LearningProfileUserBOs
   * @param {LearningProfileUserID} LearningProfileUserBO to be deleted
   * @public
   */
    deleteLearningProfileUser(learningprofileuserID){
        return this.#fetchAdvanced(this.#deleteLearningProfileUserURL(learningprofileuserID), {
            method: 'DELETE'
          }).then((responseJSON) => {
            let responseLearningProfileUserBO = LearningProfileUserBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
              resolve(responseLearningProfileUserBO);
            })
          })
    }

   /**
   * Updates a LearningProfileUser and returns a Promise, which resolves to a  LearningProfileUserBO.
   * @param {learningprofileuserBO}  LearningProfileUserBO to be updated
   * @public
   */
    updateLearningProfileUser(learningprofileuser){
        return this.#fetchAdvanced(this.#updateLearningProfileUserURL(learningprofileuser.getID()), {
            method: 'PUT',
            headers:{
            'Accept': 'application/json, text/plain',
            'Content-type': 'application/json',
            },
            body: JSON.stringify(learningprofileuser)
          }).then((responseJSON) => {
            let responseLearningProfileUserBO = LearningProfileUserBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
              resolve(responseLearningProfileUserBO);
            })
          })
    }

  /**
   * Returns a Promise, which resolves to a LearningProfileUserBO
   * @param {name} user name of the LearningProfileUser to be retrieved
   * @public
   */
    getLearningProfileUserByName(name){
      return this.#fetchAdvanced(this.#getLearningProfileUserByNameURL(name)).then((responseJSON) => {
        let LearningProfileUserBOs = LearningProfileUserBO.fromJSON(responseJSON)[0];
        return new Promise(function (resolve) {
          resolve(LearningProfileUserBOs);
      })
    })
    }




    //User

     /**
   * Returns a Promise, which resolves to an Array of ChatInvitationBOs
   *
   * @public
   */
    getAllUsers(){
        return this.#fetchAdvanced(this.#getAllUsersURL()).then((responseJSON) => {
            let userBOs = UserBO.fromJSON(responseJSON);
            return new Promise(function (resolve){
                resolve(userBOs)
            })
        })
    }

    /**
    *@param {Number} UserID
    *@public
    */
    getUserById(userID){
        return this.#fetchAdvanced(this.#getUserByIdURL(userID)).then((responseJSON) => {
            let responseUserBO = UserBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
              resolve(responseUserBO);
            })
          })
    }

      /**
   * Adds a user and returns a Promise, which resolves to a new UserBO object
   *
   * @param {userBO} projectBO to be added. The ID of the new project is set by the backend
   * @public

   */
    addUser(userBO){
        return this.#fetchAdvanced(this.#addUserURL(), {
          method: 'POST',
          headers:{
            'Accept': 'application/json, text/plain',
            'Content-type': 'application/json',
          },
          body: JSON.stringify(userBO)
            }).then((responseJSON) => {
            let responseUserBO = UserBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
              resolve(responseUserBO);
            })
          })
    }

       /**
   * Returns a Promise, which resolves to an Array of UserBOs
   * @param {UserID} userID to be deleted
   * @public
   */
    deleteUser(userID){
        return this.#fetchAdvanced(this.#deleteUserURL(userID), {
            method: 'DELETE'
          }).then((responseJSON) => {
            let responseUserBO = UserBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
              resolve(responseUserBO);
            })
          })
    }

   /**
   * Updates a user and returns a Promise, which resolves to a  userBO.
   * @param {userBO}  userBO to be updated
   * @public
   */
    updateUser(user){
        return this.#fetchAdvanced(this.#updateUserURL(user.getID()), {
            method: 'PUT',
            headers:{
            'Accept': 'application/json, text/plain',
            'Content-type': 'application/json',
            },
            body: JSON.stringify(user)
          }).then((responseJSON) => {
            let responseUserBO = UserBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
              resolve(responseUserBO);
            })
          })
    }

  /**
   * Returns a Promise, which resolves to a UserBO
   * @param {lastname} lastname of the user to be retrieved
   * @public
   */
    getUserByLastname(lastname){
      return this.#fetchAdvanced(this.#getUserByLastnameURL(lastname)).then((responseJSON) => {
        let userBOs = UserBO.fromJSON(responseJSON)[0];
        return new Promise(function (resolve) {
          resolve(userBOs);
      })
    })
    }


  /**
   * Returns a Promise, which resolves to a UserBO
   * @param {firstname} firstname of the user to be retrieved
   * @public
   */
    getUserByFirstname(firstname){
      return this.#fetchAdvanced(this.#getUserByFirstnameURL(firstname)).then((responseJSON) => {
        let userBOs = UserBO.fromJSON(responseJSON)[0];
        return new Promise(function (resolve) {
          resolve(userBOs);
      })
    })
    }


      /**
   * Returns a Promise, which resolves to a UserBO
   * @param {email} Email of the user to be retrieved
   * @public
   */
    getUserByMail(email){
      return this.#fetchAdvanced(this.#getUserByMailURL(email)).then((responseJSON) => {
        let userBOs = UserBO.fromJSON(responseJSON)[0];
        return new Promise(function (resolve) {
          resolve(userBOs);
      })
    })
    }


         /**
   * Returns a Promise, which resolves to a UserBO
   * @param {googleID} Email of the user to be retrieved
   * @public
   */
    getUserByGoogleId(googleID){
      return this.#fetchAdvanced(this.#getUserByGoogleIdURL(googleID)).then((responseJSON) => {
        let userBOs = UserBO.fromJSON(responseJSON)[0];
        return new Promise(function (resolve) {
          resolve(userBOs);
      })
    })
    }


             /**
   * Returns a Promise, which resolves to a UserBO
   * @param {learningprofileID} Learningprofile of the user to be retrieved
   * @public
   */
    /**getUserByLearningProfileId(learningprofileID){
      return this.#fetchAdvanced(this.#getUserByLearningProfileIdURL(learningprofileID)).then((responseJSON) => {
        let userBOs = UserBO.fromJSON(responseJSON)[0];
        return new Promise(function (resolve) {
          resolve(userBOs);
      })
    })
    }
    */


    //Chtainvitation

     /**
   * Returns a Promise, which resolves to an Array of ChatInvitationBOs
   *
   * @public
   */
    getAllChatInvitations(){
        return this.#fetchAdvanced(this.#getAllChatInvitationsURL()).then((responseJSON) => {
            let chatinvitationBOs = ChatInvitationBO.fromJSON(responseJSON);
            return new Promise(function (resolve){
                resolve(chatinvitationBOs)
            })
        })
    }

    /**
    *@param {Number} ChatinvitationID
    *@public
    */
    getChatInvitation(chatinvitationID){
        return this.#fetchAdvanced(this.#getChatInvitationURL(chatinvitationID)).then((responseJSON) => {
            let responseChatInvitationBO = ChatInvitationBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
              resolve(responseChatInvitationBO);
            })
          })
    }

      /**
   * Adds a chatinvitation and returns a Promise, which resolves to a new ChatInvitationBO object
   *
   * @param {ChatinvitationBO} projectBO to be added. The ID of the new project is set by the backend
   * @public

   */
    addChatInvitation(chatinvitationBO){
        return this.#fetchAdvanced(this.#addChatInvitationURL(), {
          method: 'POST',
          headers:{
            'Accept': 'application/json, text/plain',
            'Content-type': 'application/json',
          },
          body: JSON.stringify(chatinvitationBO)
            }).then((responseJSON) => {
            let responseChatInvitationBO = ChatInvitationBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
              resolve(responseChatInvitationBO);
            })
          })
    }

       /**
   * Returns a Promise, which resolves to an Array of ChatinvitationBOs
   * @param {chatinvitationID} chatinvitationID to be deleted
   * @public
   */
    deleteChatInvitation(chatinvitationID){
        return this.#fetchAdvanced(this.#deleteChatInvitationURL(chatinvitationID), {
            method: 'DELETE'
          }).then((responseJSON) => {
            let responseChatInvitationBO = ChatInvitationBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
              resolve(responseChatInvitationBO);
            })
          })
    }

   /**
   * Updates a chatinvitation and returns a Promise, which resolves to a  chatinvitationBO.
   * @param {chatinvitationBO}  chatinvitationBO to be updated
   * @public
   */
    updateChatInvitation(chatinvitation){
        return this.#fetchAdvanced(this.#updateChatInvitationURL(chatinvitation.getID()), {
            method: 'PUT',
            headers:{
            'Accept': 'application/json, text/plain',
            'Content-type': 'application/json',
            },
            body: JSON.stringify(chatinvitation)
          }).then((responseJSON) => {
            let responseChatInvitationBO = ChatInvitationBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
              resolve(responseChatInvitationBO);
            })
          })
    }

  /**
   * Returns a Promise, which resolves to a ChatInvitationBO
   * @param {tuser} target_user id of the project to be retrieved
   * @public
   */
    getChatInvitationByTargetUser(tuser){
      return this.#fetchAdvanced(this.#getChatInvitationByTargetUserURL(tuser)).then((responseJSON) => {
        let chatinvitationBOs = ChatInvitationBO.fromJSON(responseJSON)[0];
        return new Promise(function (resolve) {
          resolve(chatinvitationBOs);
      })
    })
    }

  /**
   * Returns a Promise, which resolves to a ChatInvitationBO
   * @param {suser} source_user id of the project to be retrieved
   * @public
   */
    getChatInvitationBySourceUser(suser){
      return this.#fetchAdvanced(this.#getChatInvitationBySourceUserURL(suser)).then((responseJSON) => {
        let chatinvitationBOs = ChatInvitationBO.fromJSON(responseJSON)[0];
        return new Promise(function (resolve) {
          resolve(chatinvitationBOs);
      })
    })
    }


  /**
   * Returns a Promise, which resolves to a ChatInvitationBO
   * @param {chat} chat_id id of the project to be retrieved
   * @public
   */
    getChatInvitationByChat(chat){
      return this.#fetchAdvanced(this.#getChatInvitationByChatURL(chat)).then((responseJSON) => {
        let chatinvitationBOs = ChatInvitationBO.fromJSON(responseJSON)[0];
        return new Promise(function (resolve) {
          resolve(chatinvitationBOs);
      })
    })
    }
     /**
   * Returns a Promise, which resolves to an Array of Pending ChatInvitationBOs
   *
   * @public
   */
    getChatInvitationPendInvites(){
        return this.#fetchAdvanced(this.#getChatInvitationPendInvitesURL()).then((responseJSON) => {
            let chatinvitationBOs = ChatInvitationBO.fromJSON(responseJSON);
            return new Promise(function (resolve){
                resolve(chatinvitationBOs)
            })
        })
    }

      /**
   * Returns a Promise, which resolves to a ChatInvitationBO
   * @param {tuser} pending target_user id of the project to be retrieved
   * @public
   */
    getChatInvitationPendInvitesTarget(tuser){
      return this.#fetchAdvanced(this.#getChatInvitationPendInvitesTargetURL(tuser)).then((responseJSON) => {
        let chatinvitationBOs = ChatInvitationBO.fromJSON(responseJSON)[0];
        return new Promise(function (resolve) {
          resolve(chatinvitationBOs);
      })
    })
    }

          /**
   * Returns a Promise, which resolves to a ChatInvitationBO
   * @param {suser} pending source_user id of the project to be retrieved
   * @public
   */
    getChatInvitationPendInvitesSource(suser){
      return this.#fetchAdvanced(this.#getChatInvitationPendInvitesSourceURL(suser)).then((responseJSON) => {
        let chatinvitationBOs = ChatInvitationBO.fromJSON(responseJSON)[0];
        return new Promise(function (resolve) {
          resolve(chatinvitationBOs);
      })
    })
    }

              /**
   * Returns a Promise, which resolves to a ChatInvitationBO
   * @param {suser} accepted source_user id of the project to be retrieved
   * @public
   */
    getChatInvitationAcceptedInvitesSource(suser){
      return this.#fetchAdvanced(this.#getChatInvitationAcceptedInvitesSourceURL(suser)).then((responseJSON) => {
        let chatinvitationBOs = ChatInvitationBO.fromJSON(responseJSON)[0];
        return new Promise(function (resolve) {
          resolve(chatinvitationBOs);
      })
    })
    }

                  /**
   * Returns a Promise, which resolves to a ChatInvitationBO
   * @param {tuser} accepted source_user id of the project to be retrieved
   * @public
   */
    getChatInvitationAcceptedInvitesTarget(tuser){
      return this.#fetchAdvanced(this.#getChatInvitationAcceptedInvitesTargetURL(tuser)).then((responseJSON) => {
        let chatinvitationBOs = ChatInvitationBO.fromJSON(responseJSON)[0];
        return new Promise(function (resolve) {
          resolve(chatinvitationBOs);
      })
    })
    }


    //GroupInvitation

     /**
   * Returns a Promise, which resolves to an Array of GroupInvitationBOs
   *
   * @public
   */
    getAllGroupInvitations(){
        return this.#fetchAdvanced(this.#getAllGroupInvitationsURL()).then((responseJSON) => {
            let groupinvitationBOs = GroupInvitationBO.fromJSON(responseJSON);
            return new Promise(function (resolve){
                resolve(groupinvitationBOs)
            })
        })
    }

    /**
    *@param {Number} GroupinvitationID
    *@public
    */
    getGroupInvitation(groupinvitationID){
        return this.#fetchAdvanced(this.#getChatInvitationURL(groupinvitationID)).then((responseJSON) => {
            let responseChatInvitationBO = GroupInvitationBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
              resolve(responseChatInvitationBO);
            })
          })
    }

      /**
   * Adds a chatinvitation and returns a Promise, which resolves to a new ChatInvitationBO object
   *
   * @param {ChatinvitationBO} projectBO to be added. The ID of the new project is set by the backend
   * @public

   */
    addGroupInvitation(groupinvitationBO){
        return this.#fetchAdvanced(this.#addGroupInvitationURL(), {
          method: 'POST',
          headers:{
            'Accept': 'application/json, text/plain',
            'Content-type': 'application/json',
          },
          body: JSON.stringify(groupinvitationBO)
            }).then((responseJSON) => {
            let responseGroupInvitationBO = GroupInvitationBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
              resolve(responseGroupInvitationBO);
            })
          })
    }

       /**
   * Returns a Promise, which resolves to an Array of ChatinvitationBOs
   * @param {GroupinvitationID} GroupinvitationID to be deleted
   * @public
   */
    deleteGroupInvitation(groupinvitationID){
        return this.#fetchAdvanced(this.#deleteGroupInvitationURL(groupinvitationID), {
            method: 'DELETE'
          }).then((responseJSON) => {
            let responseGroupInvitationBO = GroupInvitationBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
              resolve(responseGroupInvitationBO);
            })
          })
    }

   /**
   * Updates a Groupinvitation and returns a Promise, which resolves to a  chatinvitationBO.
   * @param {GroupinvitationBO}  GroupinvitationBO to be updated
   * @public
   */
    updateGroupInvitation(groupinvitation){
        return this.#fetchAdvanced(this.#updateGroupInvitationURL(groupinvitation.getID()), {
            method: 'PUT',
            headers:{
            'Accept': 'application/json, text/plain',
            'Content-type': 'application/json',
            },
            body: JSON.stringify(groupinvitation)
          }).then((responseJSON) => {
            let responseGroupInvitationBO = GroupInvitationBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
              resolve(responseGroupInvitationBO);
            })
          })
    }

  /**
   * Returns a Promise, which resolves to a GroupInvitationBO
   * @param {tuser} target_user id of the user to be retrieved
   * @public
   */
    getGroupInvitationByTargetUser(tuser){
      return this.#fetchAdvanced(this.#getGroupInvitationByTargetUserURL(tuser)).then((responseJSON) => {
        let groupinvitationBOs = GroupInvitationBO.fromJSON(responseJSON)[0];
        return new Promise(function (resolve) {
          resolve(groupinvitationBOs);
      })
    })
    }

  /**
   * Returns a Promise, which resolves to a ChatInvitationBO
   * @param {suser} source_user id of the user to be retrieved
   * @public
   */
    getGroupInvitationBySourceUser(suser){
      return this.#fetchAdvanced(this.#getGroupInvitationBySourceUserURL(suser)).then((responseJSON) => {
        let groupinvitationBOs = GroupInvitationBO.fromJSON(responseJSON)[0];
        return new Promise(function (resolve) {
          resolve(groupinvitationBOs);
      })
    })
    }


  /**
   * Returns a Promise, which resolves to a ChatInvitationBO
   * @param {sgroup} studygroup of the Groupinvitation to be retrieved
   * @public
   */
    getGroupInvitationByStudyGroup(sgroup){
      return this.#fetchAdvanced(this.#getGroupInvitationByStudyGroupURL(sgroup)).then((responseJSON) => {
        let groupinvitationBOs = GroupInvitationBO.fromJSON(responseJSON)[0];
        return new Promise(function (resolve) {
          resolve(groupinvitationBOs);
      })
    })
    }
     /**
   * Returns a Promise, which resolves to an Array of Pending ChatInvitationBOs
   *
   * @public
   */
    getGroupInvitationPendInvites(){
        return this.#fetchAdvanced(this.#getGroupInvitationPendInvitesURL()).then((responseJSON) => {
            let groupinvitationBOs = GroupInvitationBO.fromJSON(responseJSON);
            return new Promise(function (resolve){
                resolve(groupinvitationBOs)
            })
        })
    }

      /**
   * Returns a Promise, which resolves to a GroupInvitationBO
   * @param {tuser} pending target_user id of the project to be retrieved
   * @public
   */
    getGroupInvitationPendInvitesTarget(tuser){
      return this.#fetchAdvanced(this.#getGroupInvitationPendInvitesTargetURL(tuser)).then((responseJSON) => {
        let groupinvitationBOs = GroupInvitationBO.fromJSON(responseJSON)[0];
        return new Promise(function (resolve) {
          resolve(groupinvitationBOs);
      })
    })
    }

          /**
   * Returns a Promise, which resolves to a GroupInvitationBO
   * @param {suser} pending source_user id of the project to be retrieved
   * @public
   */
    getGroupInvitationPendInvitesSource(suser){
      return this.#fetchAdvanced(this.#getGroupInvitationPendInvitesSourceURL(suser)).then((responseJSON) => {
        let groupinvitationBOs = GroupInvitationBO.fromJSON(responseJSON)[0];
        return new Promise(function (resolve) {
          resolve(groupinvitationBOs);
      })
    })
    }

              /**
   * Returns a Promise, which resolves to a ChatInvitationBO
   * @param {suser} accepted source_user id of the project to be retrieved
   * @public
   */
    getGroupInvitationAcceptedInvitesSource(suser){
      return this.#fetchAdvanced(this.#getGroupInvitationAcceptedInvitesSourceURL(suser)).then((responseJSON) => {
        let groupinvitationBOs = GroupInvitationBO.fromJSON(responseJSON)[0];
        return new Promise(function (resolve) {
          resolve(groupinvitationBOs);
      })
    })
    }

                  /**
   * Returns a Promise, which resolves to a GroupInvitationBO, pretty sus ngl
   * @param {suser} accepted source_user id of the project to be retrieved
   * @public
   */
    getGroupInvitationAcceptedInvitesTarget(tuser){
      return this.#fetchAdvanced(this.#getGroupInvitationAcceptedInvitesTargetURL(tuser)).then((responseJSON) => {
        let groupinvitationBOs = GroupInvitationBO.fromJSON(responseJSON)[0];
        return new Promise(function (resolve) {
          resolve(groupinvitationBOs);
      })
    })
    }

                    /**
   * Returns a Promise, which resolves to a GroupInvitationBO
   * @param {suser} accepted source_user id of the project to be retrieved
   * @public
   */
    getMatchesUser(tuser){
      return this.#fetchAdvanced(this.#getMatches(tuser)).then((responseJSON) => {
        let matches = UserMatchBO.fromJSON(responseJSON);
        return new Promise(function (resolve) {
          resolve(matches);
      })
    })
    }
                        /**
   * Returns a Promise, which resolves to a GroupInvitationBO
   * @param {suser} accepted source_user id of the project to be retrieved
   * @public
   */
    getMatchesGroup(tuser){
      return this.#fetchAdvanced(this.#getGroupMatches(tuser)).then((responseJSON) => {
        let matches = GroupMatchBO.fromJSON(responseJSON);
        return new Promise(function (resolve) {
          resolve(matches);
      })
    })
    }

    getAuth(){
      return this.#fetchAdvanced(this.#getAuth())

    }
                          /**
     * Returns a Promise, which resolves to a GroupInvitationBO
     * @param {suser} accepted source_user id of the project to be retrieved
     * @public
     */
    
    getFriendsByGoogleId(user){
      return this.#fetchAdvanced(this.#getFriendsByGoogleId(user)).then((responseJSON) => {
        let users = UserBO.fromJSON(responseJSON);
        return new Promise(function (resolve) {
          resolve(users);
      })
    })
    }
                        /**
     * Returns a Promise, which resolves to a GroupInvitationBO
     * @param {suser} accepted source_user id of the project to be retrieved
     * @public
     */

    getFriendRequestsByGoogleId(user){
      return this.#fetchAdvanced(this.#getFriendRequestsByGoogleId(user)).then((responseJSON) => {
        let users = UserBO.fromJSON(responseJSON);
        return new Promise(function (resolve) {
          resolve(users);
        })
      })
      }

    getGroupsByGoogleId(user){
      return this.#fetchAdvanced(this.#getGroupsByGoogleId(user)).then((responseJSON) => {
        let users = StudyGroupBO.fromJSON(responseJSON);
        return new Promise(function (resolve) {
          resolve(users);
        })
      })
      }


    getUserPendingGroupInvites(id){
      return this.#fetchAdvanced(this.#getUserPendingGroupInvites(id)).then((responseJSON) => {
        let users = UserBO.fromJSON(responseJSON);
        return new Promise(function (resolve) {
          resolve(users);
        })
      })
      }

    acceptFriendRequest(target_id, source_id){
      return this.#fetchAdvanced(this.#acceptFriendRequest(target_id, source_id))
      }

    declineFriendRequest(target_id, source_id){
      return this.#fetchAdvanced(this.#declineFriendRequest(target_id, source_id))
      }


    getChatByUserId(id){
      return this.#fetchAdvanced(this.#getChatByUserId(id)).then((responseJSON) => {
        let chats = ChatBO.fromJSON(responseJSON);
        return new Promise(function (resolve) {
          resolve(chats);
        })
      })
      }

    getOtherUserByChatId(current_user, chat_id){
      return this.#fetchAdvanced(this.#getOtherUserByChatId(current_user, chat_id)).then((responseJSON) => {
        let chats = UserBO.fromJSON(responseJSON);
        return new Promise(function (resolve) {
          resolve(chats);
        })
      })
      }

      removeFriend(target_id, source_id){
        return this.#fetchAdvanced(this.#removeFriend(target_id, source_id))
        }
      
      leaveGroup(target_id, group_id){
        return this.#fetchAdvanced(this.#leaveGroup(target_id, group_id))
        }

  }
