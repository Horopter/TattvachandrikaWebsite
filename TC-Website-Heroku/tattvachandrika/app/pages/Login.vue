<template>
  <div class="bg-amber-50 min-h-screen">
    <!-- Header -->
    <header class="bg-orange-50">
      <div class="container mx-auto flex justify-between items-center p-4">
        <h1 class="text-xl font-bold text-orange-700">Hari Sarvottama</h1>
        <img src="../assets/images/Hanuma1.png" alt="hanuma" />
        <div class="relative flex flex-col items-center">
          <svg width="300" height="200">
            <defs>
              <path
                id="curve"
                d="M 150, 150 m -100, 0 a 100,100 0 1,1 200,0 a 100,100 0 1,1 -200,0"
              />
            </defs>
            <text>
              <textPath
                xlink:href="#curve"
                startOffset="25%"
                text-anchor="middle"
              >
                Sri Moola Gopala Krishno Vijayathe
              </textPath>
            </text>
          </svg>
          <img
            src="../assets/images/GopalaKrishna.png"
            alt="krishna"
            class="w-24 h-24 rounded-full absolute"
            style="top: 80px; left: 50%; transform: translateX(-50%)"
          />
        </div>
        <img src="../assets/images/hanuma2.png" alt="Bheema" />
        <h1 class="text-xl font-bold text-orange-700">Vaayu Jeevottama</h1>
      </div>
    </header>

    <!-- Main content -->
    <main class="container mx-auto mt-6 p-6">
      <div class="bg-white rounded-lg shadow-lg p-6 mt-4">
        <h2 class="text-3xl font-bold text-center mb-4 text-orange-800">
          Welcome to Sri Tatwa Chandrika
        </h2>

        <div class="tabs mb-6">
          <button
            @click="toggleTab('login')"
            :class="{ active: currentTab === 'login' }"
            class="tab-button"
          >
            Login
          </button>
          <button
            @click="toggleTab('signup')"
            :class="{ active: currentTab === 'signup' }"
            class="tab-button"
          >
            Sign Up
          </button>
        </div>

        <div v-if="currentTab === 'login'" class="form">
          <h2 class="text-xl font-bold text-center">Login</h2>
          <form @submit.prevent="login">
            <input
              v-model="loginData.username"
              type="text"
              placeholder="Username"
              required
              class="input-field"
            />
            <input
              v-model="loginData.password"
              type="password"
              placeholder="Password"
              required
              class="input-field"
            />
            <button type="submit" class="submit-button">Login</button>
          </form>
        </div>

        <div v-if="currentTab === 'signup'" class="form">
          <h2 class="text-xl font-bold text-center">Sign Up</h2>
          <form @submit.prevent="signup">
            <input
              v-model="signupData.first_name"
              type="text"
              placeholder="First Name"
              required
              class="input-field"
            />
            <span v-if="errors.first_name" class="error-message">{{
              errors.first_name
            }}</span>

            <input
              v-model="signupData.last_name"
              type="text"
              placeholder="Last Name"
              required
              class="input-field"
            />
            <span v-if="errors.last_name" class="error-message">{{
              errors.last_name
            }}</span>

            <input
              v-model="signupData.username"
              type="text"
              placeholder="Username"
              required
              class="input-field"
            />
            <span v-if="errors.username" class="error-message">{{
              errors.username
            }}</span>

            <input
              v-model="signupData.email"
              type="email"
              placeholder="Email"
              required
              class="input-field"
            />
            <span v-if="errors.email" class="error-message">{{
              errors.email
            }}</span>

            <input
              v-model="signupData.aadhaar"
              type="text"
              placeholder="Aadhaar Number"
              required
              class="input-field"
            />
            <span v-if="errors.aadhaar" class="error-message">{{
              errors.aadhaar
            }}</span>

            <input
              v-model="signupData.mobile"
              type="text"
              placeholder="Mobile Number"
              required
              class="input-field"
            />
            <span v-if="errors.mobile" class="error-message">{{
              errors.mobile
            }}</span>

            <input
              v-model="signupData.password"
              type="password"
              placeholder="Password"
              required
              class="input-field"
            />
            <span v-if="errors.password" class="error-message">{{
              errors.password
            }}</span>

            <input
              v-model="signupData.re_password"
              type="password"
              placeholder="Re-enter Password"
              required
              class="input-field"
            />
            <span v-if="errors.re_password" class="error-message">{{
              errors.re_password
            }}</span>

            <button type="submit" class="submit-button">Sign Up</button>
          </form>
        </div>

        <toast-message
          v-if="toastVisible"
          :message="toastMessage"
          @close="toastVisible = false"
        />
      </div>
    </main>
  </div>
</template>

<script>
import axios from "axios"; // Ensure axios is installed and imported
import ToastMessage from "./ToastMessage.vue"; // A simple toast message component

export default {
  components: {
    ToastMessage,
  },
  data() {
    return {
      currentTab: "login",
      loginData: {
        username: "",
        password: "",
      },
      signupData: {
        first_name: "",
        last_name: "",
        username: "",
        email: "",
        aadhaar: "",
        mobile: "",
        password: "",
        re_password: "",
      },
      errors: {}, // Object to hold validation errors
      toastVisible: false,
      toastMessage: "",
    };
  },
  methods: {
    toggleTab(tab) {
      this.currentTab = tab;
      this.errors = {}; // Reset errors when switching tabs
    },
    validateSignup() {
      this.errors = {};
      let isValid = true;

      // Validate first name
      if (!this.signupData.first_name) {
        this.errors.first_name = "First Name is required.";
        isValid = false;
      }

      // Validate last name
      if (!this.signupData.last_name) {
        this.errors.last_name = "Last Name is required.";
        isValid = false;
      }

      // Validate username
      if (!this.signupData.username) {
        this.errors.username = "Username is required.";
        isValid = false;
      }

      // Validate email
      const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!this.signupData.email) {
        this.errors.email = "Email is required.";
        isValid = false;
      } else if (!emailPattern.test(this.signupData.email)) {
        this.errors.email = "Invalid email format.";
        isValid = false;
      }

      // Validate Aadhaar number
      if (!this.signupData.aadhaar) {
        this.errors.aadhaar = "Aadhaar Number is required.";
        isValid = false;
      }

      // Validate mobile number
      const mobilePattern = /^[0-9]{10}$/; // Simple validation for 10-digit number
      if (!this.signupData.mobile) {
        this.errors.mobile = "Mobile Number is required.";
        isValid = false;
      } else if (!mobilePattern.test(this.signupData.mobile)) {
        this.errors.mobile = "Invalid mobile number format.";
        isValid = false;
      }

      // Validate password
      if (!this.signupData.password) {
        this.errors.password = "Password is required.";
        isValid = false;
      }

      // Validate re-entered password
      if (this.signupData.password !== this.signupData.re_password) {
        this.errors.re_password = "Passwords do not match.";
        isValid = false;
      }

      return isValid;
    },
    async login() {
      try {
        const response = await axios.post(
          "https://tattvachandrika-magazine-119814d66a82.herokuapp.com/api/adminusers/login/",
          this.loginData
        );
        localStorage.setItem('token', response.data.token);
        this.$router.push({ name: "HomePage" }); // Redirect to homepage
      } catch (error) {
        console.error("Login failed:", error.response.data);
        alert("Login failed: " + error.response.data.error);
      }
    },
    async signup() {
      if (this.validateSignup()) {
        // Only proceed if validation is successful
        try {
          const response = await axios.post(
            "https://tattvachandrika-magazine-119814d66a82.herokuapp.com/api/adminusers/signup/",
            {
              username: this.signupData.username,
              email: this.signupData.email,
              first_name: this.signupData.first_name,
              last_name: this.signupData.last_name,
              aadhaar: this.signupData.aadhaar,
              mobile: this.signupData.mobile,
              password: this.signupData.password,
            }
          );
          console.log(response.data);
          this.toastMessage = "Sign up successful! Please log in.";
          this.toastVisible = true;
          this.toggleTab("login"); // Switch to login tab after successful signup
        } catch (error) {
          console.error("Sign up failed:", error);
          // Check if the error has a response object
          if (error.response && error.response.data) {
            alert(
              "Sign up failed: " +
                (error.response.data.error ||
                  error.response.data.detail ||
                  "Unknown error")
            );
          } else {
            alert("Sign up failed: " + (error.message || "Network error"));
          }
        }
      }
    },
  },
};
</script>

<style scoped>
.bg-amber-50 {
  background-color: #fbbf24; /* Amber background */
}
.bg-orange-50 {
  background-color: #feebc8; /* Light orange background */
}
.bg-orange-100 {
  background-color: #ffedd5; /* Even lighter orange */
}
.text-orange-700 {
  color: #b45309; /* Darker orange */
}
.text-orange-800 {
  color: #9a3412; /* Darker orange for headers */
}
.container {
  max-width: 600px;
}
.tabs {
  display: flex;
  justify-content: space-between;
  margin-bottom: 20px;
}
.tab-button {
  flex: 1;
  padding: 10px;
  cursor: pointer;
  background-color: transparent;
  border: 1px solid #feab00; /* Light orange border */
  color: #b45309; /* Dark orange text */
  transition: background-color 0.3s, color 0.3s;
}
.tab-button.active {
  background-color: #feab00; /* Light orange background when active */
  color: white; /* White text */
}
.input-field {
  width: 100%;
  padding: 10px;
  margin: 10px 0;
  border: 1px solid #ccc;
  border-radius: 4px;
}
.submit-button {
  width: 100%;
  padding: 10px;
  background-color: #feab00; /* Light orange */
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
}
.submit-button:hover {
  background-color: #e9b300; /* Darker light orange on hover */
}
.error-message {
  color: red;
  font-size: 0.875rem;
}
</style>
