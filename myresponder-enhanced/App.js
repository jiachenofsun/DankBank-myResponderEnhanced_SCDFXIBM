import * as React from 'react';
import { Text, View } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import defaultscreen from './screens/defaultscreen';
import webpage from './screens/webpage';
import FontAwesome from 'react-native-vector-icons/FontAwesome';

const Tab = createBottomTabNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Tab.Navigator
        screenOptions={({ route }) => ({
          tabBarIcon: ({ focused, color, size }) => {
            let iconName;

            if (route.name === 'Home') {
              iconName = 'home';
            } else if (route.name === 'Notification') {
              iconName = 'clipboard';
            } else if (route.name === '995') {
              iconName = 'phone';
            } else if (route.name === 'Camera') {
              iconName = 'camera';
            } else if (route.name === 'AED') {
              iconName = 'briefcase';
            } else if (route.name === 'Help') {
              iconName = 'plus';
            }

            return <FontAwesome name={iconName} size={size} color={color} />;
          },
        })}
        tabBarOptions={{
          activeTintColor: 'red',
          inactiveTintColor: 'gray',
        }}>
        <Tab.Screen name="Home" component={defaultscreen} />
        <Tab.Screen name="Notification" component={defaultscreen} />
        <Tab.Screen name="995" component={defaultscreen} />
        <Tab.Screen name="Camera" component={defaultscreen} />
        <Tab.Screen name="AED" component={defaultscreen} />
        <Tab.Screen name="Help" component={webpage} />
      </Tab.Navigator>
    </NavigationContainer>
  );
}
