import * as React from "react";
import { Text, View, Image, StyleSheet } from "react-native";
import { FontAwesome } from "@expo/vector-icons";

export default function HomeScreen() {
  return (
    <View
      style={styles.container}
    >
      <Image
        style={styles.interface}
        source={require('../assets/homepage.jpg')}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    padding: 0,
    height: '100%',
    width: '100%',
  },
  interface: {
    height: '100%',
    width: '100%',
    resizeMode: 'contain',
  },
});