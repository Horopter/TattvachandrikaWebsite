<template>
  <div class="container mt-5">
    <!-- Breadcrumb navigation -->
    <nav aria-label="breadcrumb">
      <ol class="breadcrumb">
        <li class="breadcrumb-item"><router-link to="/">Home</router-link></li>
        <li class="breadcrumb-item active" aria-current="page">Subscription Plans</li>
      </ol>
    </nav>

    <!-- Page Title -->
    <h2>Subscription Plans</h2>

    <!-- Button to add a new subscription plan -->
    <button class="btn btn-primary mb-3" @click="addPlan">Add Subscription Plan</button>

    <!-- Table displaying the subscription plans -->
    <table class="table table-striped">
      <thead>
        <tr>
          <th>Name</th>
          <th>Version</th>
          <th>Start Date</th>
          <th>Price</th>
          <th>Language</th>
          <th>Mode</th>
          <th>Duration (Months)</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <!-- Iterate over each plan in plans array -->
        <tr v-for="plan in plans" :key="plan._id">
          <td>{{ plan.name }}</td>
          <td>{{ plan.version }}</td>
          <td>
            <!-- Editable start date only when adding a new plan -->
            <input v-if="editPlanId === plan._id && isAddingNew" type="date" v-model="plan.start_date" />
            <span v-else>{{ plan.start_date }}</span>
          </td>
          <td>
            <!-- Editable price field -->
            <input v-if="editPlanId === plan._id" type="number" v-model="plan.subscription_price" />
            <span v-else>{{ plan.subscription_price }}</span>
          </td>
          <td>
            <!-- Editable language dropdown -->
            <select v-if="editPlanId === plan._id" v-model="plan.subscription_language" :key="plan._id + '_language'">
              <option v-for="language in languages" :value="language._id" :key="language._id">{{ language.name }}</option>
            </select>
            <span v-else>{{ getLanguageName(plan.subscription_language) }}</span>
          </td>
          <td>
            <!-- Editable mode dropdown -->
            <select v-if="editPlanId === plan._id" v-model="plan.subscription_mode" :key="plan._id + '_mode'">
              <option v-for="mode in modes" :value="mode._id" :key="mode._id">{{ mode.name }}</option>
            </select>
            <span v-else>{{ getModeName(plan.subscription_mode) }}</span>
          </td>
          <td>
            <!-- Editable duration field -->
            <input v-if="editPlanId === plan._id" type="number" v-model="plan.duration_in_months" />
            <span v-else>{{ plan.duration_in_months }}</span>
          </td>
          <td>
            <!-- Action buttons for save, edit, delete, and cancel -->
            <button class="btn btn-success btn-sm" v-if="editPlanId === plan._id" @click="savePlan(plan)">Save</button>
            <button class="btn btn-warning btn-sm" v-if="editPlanId !== plan._id" @click="editPlan(plan._id)">Edit</button>
            <button class="btn btn-secondary btn-sm" v-if="editPlanId === plan._id" @click="cancelAdd">Cancel</button>
          </td>
        </tr>
      </tbody>
    </table>

    <!-- Confirmation modal for deletion -->
    <confirmation-modal
      v-if="showConfirmationModal"
      :show="showConfirmationModal"
      title="Confirm Delete"
      message="Are you sure you want to delete this subscription plan?"
      @close="hideDeleteModal"
      @confirm="deletePlan"
    />
  </div>
</template>

<script>
import subscriptionPlanService from '../services/subscriptionPlanService';
import confirmationModal from './ConfirmationModal.vue';

export default {
  components: {
    confirmationModal
  },
  data() {
    return {
      plans: [], // Array to hold subscription plans
      languages: [], // Array to hold available languages
      modes: [], // Array to hold available modes
      editPlanId: null, // ID of the plan currently being edited
      showConfirmationModal: false, // Boolean to control the visibility of the confirmation modal
      planToDelete: null, // ID of the plan to be deleted
      isAddingNew: false // Flag to indicate if a new plan is being added
    };
  },
  created() {
    this.loadPlans();
    this.loadLanguages();
    this.loadModes();
  },
  methods: {
    // Method to load subscription plans
    loadPlans() {
      subscriptionPlanService.getPlans().then(response => {
        this.plans = response.data;
      }).catch(error => {
        console.error("There was an error retrieving the subscription plans!", error);
      });
    },
    // Method to load languages
    loadLanguages() {
      subscriptionPlanService.getLanguages().then(response => {
        this.languages = response.data;
      }).catch(error => {
        console.error("There was an error retrieving the languages!", error);
      });
    },
    // Method to load modes
    loadModes() {
      subscriptionPlanService.getModes().then(response => {
        this.modes = response.data;
      }).catch(error => {
        console.error("There was an error retrieving the modes!", error);
      });
    },
    // Method to add a new plan
    addPlan() {
      const newPlan = {
        _id: null, // New plans do not have an _id yet
        name: 'New Plan Name', // Automatically populated name
        version: '', // Version will be determined when saving
        start_date: '',
        subscription_price: 0,
        subscription_language: this.languages.length > 0 ? this.languages[0]._id : null,
        subscription_mode: this.modes.length > 0 ? this.modes[0]._id : null,
        duration_in_months: 0
      };
      this.plans.unshift(newPlan); // Add the new plan to the beginning of the plans array
      this.editPlanId = newPlan._id; // Set the new plan as the one being edited
      this.isAddingNew = true; // Indicate that a new plan is being added
    },
    // Method to edit an existing plan
    editPlan(planId) {
      this.editPlanId = planId; // Set the plan ID as the one being edited
      this.isAddingNew = false; // Indicate that we are not adding a new plan
    },
    // Method to save a plan
    async savePlan(plan) {
      // Check for existing plans with the same duration, language, and mode
      const existingPlans = this.plans.filter(p => 
        p.duration_in_months === plan.duration_in_months &&
        p.subscription_language === plan.subscription_language &&
        p.subscription_mode === plan.subscription_mode
      );

      if (existingPlans.length > 0) {
        // Filter out invalid versions (NaN or null)
        const validVersions = existingPlans.map(p => parseInt(p.version.replace('v', ''))).filter(v => !isNaN(v) && v !== null);
        // Find the highest valid version and increment it
        const highestVersion = validVersions.length > 0 ? Math.max(...validVersions) : 0;
        plan.version = 'v' + (highestVersion + 1);
      } else {
        // If no existing plans with the same attributes, set version to v1
        plan.version = 'v1';
      }

      const planData = {
        ...plan,
        subscription_language: plan.subscription_language,
        subscription_mode: plan.subscription_mode
      };
      if (plan._id) {
        // If the plan has an _id, update it
        subscriptionPlanService.updatePlan(plan._id, planData).then(() => {
          this.loadPlans(); // Reload the plans after updating
          this.editPlanId = null; // Clear the edit plan ID
        }).catch(error => {
          console.error("There was an error updating the subscription plan!", error);
        });
      } else {
        // If the plan does not have an _id, create it
        subscriptionPlanService.createPlan(planData).then(() => {
          this.loadPlans(); // Reload the plans after creating
          this.editPlanId = null; // Clear the edit plan ID
          this.isAddingNew = false; // Indicate that we are no longer adding a new plan
        }).catch(error => {
          console.error("There was an error creating the subscription plan!", error);
        });
      }
    },
    // Method to cancel adding a new plan
    cancelAdd() {
      this.editPlanId = null; // Clear the edit plan ID
      this.isAddingNew = false; // Indicate that we are no longer adding a new plan
    },
    // Method to confirm deletion of a plan
    confirmDeletePlan(planId) {
      this.planToDelete = planId; // Set the plan ID to be deleted
      this.showConfirmationModal = true; // Show the confirmation modal
    },
    // Method to hide the delete confirmation modal
    hideDeleteModal() {
      this.showConfirmationModal = false; // Hide the confirmation modal
    },
    // Method to delete a plan
    deletePlan() {
      if (this.planToDelete) {
        subscriptionPlanService.deletePlan(this.planToDelete).then(() => {
          this.loadPlans(); // Reload the plans after deleting
          this.hideDeleteModal(); // Hide the confirmation modal
        }).catch(error => {
          console.error("There was an error deleting the subscription plan!", error);
        });
      }
    },
    // Method to get the name of a language by its ID
    getLanguageName(languageId) {
      const language = this.languages.find(lang => lang._id === languageId);
      return language ? language.name : '';
    },
    // Method to get the name of a mode by its ID
    getModeName(modeId) {
      const mode = this.modes.find(m => m._id === modeId);
      return mode ? mode.name : '';
    }
  }
};
</script>

<style scoped>
/* Custom styles for the component */
.table {
  margin-top: 20px;
}
</style>
