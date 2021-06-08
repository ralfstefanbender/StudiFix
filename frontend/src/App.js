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



class App extends React.Component {


	render() {


		return (
			<ThemeProvider theme={theme}>
				<CssBaseline />
				<Router basename={process.env.PUBLIC_URL}>
					<Container maxWidth='md'>
					    <Header />

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
									<Route path='/lerngruppen'>
										<ManageStudyGroup />
									</Route>
									<Route path='/lernpartner'>
										<UserGroups />
									</Route>
									<Route exact path='/about'>
										<About />
									</Route>
					</Container>
				</Router>
			</ThemeProvider>
		);
	}
}

export default App;