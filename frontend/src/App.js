import React, { Component } from 'react';
import theme from './theme';
import Header from './components/layout/Header';
import { ThemeProvider } from '@material-ui/core/styles';
import { BrowserRouter as Router, Route, Redirect } from 'react-router-dom';
import { Container, CssBaseline } from '@material-ui/core';
import ManageChat from './components/pages/ManageChat';
import ManageStudyGroup from './components/pages/ManageStudyGroup';
import UserProfile from './components/pages/UserProfile';
import About from './components/pages/About';
import Overview from './components/pages/Overview';
import UserGroups from './components/subcomponents/UserGroups';
import CreateStudyGroup from './components/CreateStudyGroup';
import 'firebase/auth';
import SignIn from './components/pages/SignIn';
import firebase from 'firebase/app';
import LoadingProgress from './components/dialogs/LoadingProgress';
import ContextErrorMessage from './components/dialogs/ContextErrorMessage';
import firebaseConfig from './firebaseconfig';

class App extends Component {
/** Constructor of the app, which initializes firebase  */
  constructor(props) {
		super(props);

		// Init an empty state
		this.state = {
			currentUser: null,
			appError: null,
			authError: null,
			authLoading: false
		};
  }



  static getDerivedStateFromError(error) {
		// Update state so the next render will show the fallback UI.
		return { appError: error };
	}

  /** Handled das einloggen des Users -> schreibt ihn in den State  */
	handleAuthStateChange = user => {
		if (user) {
		this.setState({
				authLoading: true
			});
			// The user is signed in
			user.getIdToken().then(token => {
				// Add the token to the browser's cookies. The server will then be
				// able to verify the token against the API.
				// SECURITY NOTE: As cookies can easily be modified, only put the
				// token (which is verified server-side) in a cookie; do not add other
				// user information.
				document.cookie = `token=${token};path=/`;

				// Set the user not before the token arrived
				this.setState({
					currentUser: user,
					authError: null,
					authLoading: false
				});
			}).catch(e => {
				this.setState({
					authError: e,
					authLoading: false
				});
			});
		} else {
			// User has logged out, so clear the id token
			document.cookie = 'token=;path=/';

			// Set the logged out user to null
			this.setState({
				currentUser: null,
				authLoading: false
			});
		}
	}

	/**
   * Handles the sign in request of the SignIn component uses the firebase.auth() component to sign in.
	 * @see See Google [firebase.auth()](https://firebase.google.com/docs/reference/js/firebase.auth.Auth)
	 * @see See Google [firebase.auth().signInWithRedirect](https://firebase.google.com/docs/reference/js/firebase.auth.Auth#signinwithredirect)
	 */
	 handleSignIn = () => {
		const provider = new firebase.auth.GoogleAuthProvider();
		firebase.auth().signInWithRedirect(provider);
	}

	/**
	 * Lifecycle method, which is called when the component gets inserted into the browsers DOM.
	 * Initializes the firebase SDK.
	 *
	 * @see See Googles [firebase init process](https://firebase.google.com/docs/web/setup)
	 */
	componentDidMount() {
		firebase.initializeApp(firebaseConfig);
		firebase.auth().languageCode = 'de';
		firebase.auth().onAuthStateChanged(this.handleAuthStateChange);
	}

	render() {
	        const { currentUser, appError, authError, authLoading } = this.state;



		return (
			<ThemeProvider theme={theme}>
				<div>
				<CssBaseline />
				<Router basename={process.env.PUBLIC_URL}>
					<Container maxWidth='md'>
						<Header user={currentUser} />
						{
							// Is a user signed in?
							currentUser ?
                                <>
								    <Redirect from='/' to='user' />
								    <Route exact path='/overview'>
										<Overview />
									</Route>
									<Route exact path='/user'>
										<UserProfile />
									</Route>
									<Route path='/chat'>
										<ManageChat />
									</Route>
									<Route path='/studygroup'>
										<CreateStudyGroup />
									</Route>
									<Route path='/lernpartner'>
										<UserGroups />
									</Route>
									<Route exact path='/about'>
										<About />
									</Route>

					</> :
				// elso show the sign in page
				<>
				<Redirect to='/index.html'/>
				<SignIn onSignIn={this.handleSignIn}/>

				</>

			}

			         <LoadingProgress show={authLoading} />
					<ContextErrorMessage error={authError} contextErrorMsg={`Something went wrong during sighn in process.`} onReload={this.handleSignIn} />
					<ContextErrorMessage error={appError} contextErrorMsg={`Something went wrong inside the app. Please reload the page.`} />
					</Container>
				</Router>
				</div>
			</ThemeProvider>
		);
	}
}

export default App;