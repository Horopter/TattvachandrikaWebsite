<template>
  <div class="container mx-auto mt-5 px-4">
    <!-- Breadcrumb navigation -->
    <nav aria-label="breadcrumb" class="mb-4">
      <ol class="flex space-x-2 text-gray-700">
        <li>
          <router-link to="/" class="text-blue-600 hover:text-blue-800">Home</router-link>
        </li>
        <li>
          <span>/</span>
        </li>
        <li class="text-gray-500" aria-current="page">Subscription Plans</li>
      </ol>
    </nav>

    <!-- Page Title -->
    <h2 class="text-2xl font-bold text-gray-800 mb-4">Subscription Plans</h2>

    <!-- Button to add a new subscription plan -->
    <div class="flex justify-end mb-4">
      <button class="bg-blue-600 text-white px-4 py-2 rounded-md shadow-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500" @click="addPlan">Add Subscription Plan</button>
    </div>

    <!-- Table displaying the subscription plans -->
    <div class="overflow-x-auto">
      <table class="min-w-full bg-white border border-gray-200 shadow-md rounded-lg">
        <thead class="bg-gray-100">
          <tr>
            <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Name</th>
            <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Version</th>
            <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Start Date</th>
            <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Price</th>
            <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Language</th>
            <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Mode</th>
            <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Duration (Months)</th>
            <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Actions</th>
          </tr>
        </thead>
        <tbody class="bg-white divide-y divide-gray-200">
          <!-- Iterate over each plan in plans array -->
          <tr v-for="plan in plans" :key="plan._id" class="hover:bg-gray-50">
            <td class="px-4 py-4 text-lg text-gray-900">{{ plan.name }}</td>
            <td class="px-4 py-4 text-sm text-gray-900">{{ plan.version }}</td>
            <td class="px-4 py-4 text-sm text-gray-900">
              <input v-if="editPlanId === plan._id && isAddingNew" type="date" v-model="plan.start_date" class="border border-gray-300 px-2 py-1 rounded-md w-full" />
              <span v-else>{{ plan.start_date }}</span>
            </td>
            <td class="px-4 py-4 text-sm text-gray-900">
              <input v-if="editPlanId === plan._id" type="number" v-model="plan.subscription_price" class="border border-gray-300 px-2 py-1 rounded-md w-full" />
              <span v-else>{{ plan.subscription_price }}</span>
            </td>
            <td class="px-4 py-4 text-sm text-gray-900">
              <select v-if="editPlanId === plan._id" v-model="plan.subscription_language" class="border border-gray-300 px-2 py-1 rounded-md w-full">
                <option v-for="language in languages" :value="language._id" :key="language._id">{{ language.name }}</option>
              </select>
              <span v-else>{{ getLanguageName(plan.subscription_language) }}</span>
            </td>
            <td class="px-4 py-4 text-sm text-gray-900">
              <select v-if="editPlanId === plan._id" v-model="plan.subscription_mode" class="border border-gray-300 px-2 py-1 rounded-md w-full">
                <option v-for="mode in modes" :value="mode._id" :key="mode._id">{{ mode.name }}</option>
              </select>
              <span v-else>{{ getModeName(plan.subscription_mode) }}</span>
            </td>
            <td class="px-4 py-4 text-sm text-gray-900">
              <input v-if="editPlanId === plan._id" type="number" v-model="plan.duration_in_months" class="border border-gray-300 px-2 py-1 rounded-md w-full" />
              <span v-else>{{ plan.duration_in_months }}</span>
            </td>
            <td class="px-4 py-4 text-sm text-gray-900 flex space-x-2">
              <button v-if="editPlanId === plan._id" @click="savePlan(plan)" class="bg-green-600 text-white px-3 py-1 rounded-md text-xs shadow-sm hover:bg-green-700">Save</button>
              <button v-if="editPlanId !== plan._id" @click="editPlan(plan._id)" class="bg-yellow-500 text-white px-3 py-1 rounded-md text-xs shadow-sm hover:bg-yellow-600">Edit</button>
              <button v-if="editPlanId === plan._id" @click="cancelAdd" class="bg-gray-500 text-white px-3 py-1 rounded-md text-xs shadow-sm hover:bg-gray-600">Cancel</button>
              <button @click="confirmDeletePlan(plan._id)" class="bg-red-600 text-white px-3 py-1 rounded-md text-xs shadow-sm hover:bg-red-700">Delete</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

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
      plans: [],
      languages: [],
      modes: [],
      editPlanId: null,
      showConfirmationModal: false,
      planToDelete: null,
      isAddingNew: false
    };
  },
  created() {
    this.loadPlans();
    this.loadLanguages();
    this.loadModes();
  },
  methods: {
    loadPlans() {
      subscriptionPlanService.getPlans().then(response => {
        this.plans = response.data;
      }).catch(error => {
        console.error("There was an error retrieving the subscription plans!", error);
      });
    },
    loadLanguages() {
      subscriptionPlanService.getLanguages().then(response => {
        this.languages = response.data;
      }).catch(error => {
        console.error("There was an error retrieving the languages!", error);
      });
    },
    loadModes() {
      subscriptionPlanService.getModes().then(response => {
        this.modes = response.data;
      }).catch(error => {
        console.error("There was an error retrieving the modes!", error);
      });
    },
    addPlan() {
      const newPlan = {
        _id: null,
        name: 'New Plan',
        version: '',
        start_date: '',
        subscription_price: 0,
        subscription_language: this.languages.length > 0 ? this.languages[0]._id : null,
        subscription_mode: this.modes.length > 0 ? this.modes[0]._id : null,
        duration_in_months: 0
      };
      this.plans.unshift(newPlan);
      this.editPlanId = newPlan._id;
      this.isAddingNew = true;
    },
    editPlan(planId) {
      this.editPlanId = planId;
      this.isAddingNew = false;
    },
    async savePlan(plan) {
      const existingPlans = this.plans.filter(p =>
        p.duration_in_months === plan.duration_in_months &&
        p.subscription_language === plan.subscription_language &&
        p.subscription_mode === plan.subscription_mode
      );

      if (existingPlans.length > 0) {
        const validVersions = existingPlans.map(p => parseInt(p.version.replace('v', ''))).filter(v => !isNaN(v) && v !== null);
        const highestVersion = validVersions.length > 0 ? Math.max(...validVersions) : 0;
        plan.version = 'v' + (highestVersion + 1);
      } else {
        plan.version = 'v1';
      }

      const planData = {
        ...plan,
        subscription_language: plan.subscription_language,
        subscription_mode: plan.subscription_mode
      };
      if (plan._id) {
        subscriptionPlanService.updatePlan(plan._id, planData).then(() => {
          this.loadPlans();
          this.editPlanId = null;
        }).catch(error => {
          console.error("There was an error updating the subscription plan!", error);
        });
      } else {
        subscriptionPlanService.createPlan(planData).then(() => {
          this.loadPlans();
          this.editPlanId = null;
          this.isAddingNew = false;
        }).catch(error => {
          console.error("There was an error creating the subscription plan!", error);
        });
      }
    },
    cancelAdd() {
      this.editPlanId = null;
      this.isAddingNew = false;
    },
    confirmDeletePlan(planId) {
      this.planToDelete = planId;
      this.showConfirmationModal = true;
    },
    hideDeleteModal() {
      this.showConfirmationModal = false;
    },
    deletePlan() {
      if (this.planToDelete) {
        subscriptionPlanService.deletePlan(this.planToDelete).then(() => {
          this.loadPlans();
          this.hideDeleteModal();
        }).catch(error => {
          console.error("There was an error deleting the subscription plan!", error);
        });
      }
    },
    getLanguageName(languageId) {
      const language = this.languages.find(lang => lang._id === languageId);
      return language ? language.name : '';
    },
    getModeName(modeId) {
      const mode = this.modes.find(m => m._id === modeId);
      return mode ? mode.name : '';
    }
  }
};
</script>

<style scoped>
.container {
  max-width: 1200px;
}
.table th, .table td {
  padding: 12px 16px;
  text-align: left;
}
.table th {
  background-color: #f8fafc;
}
</style>
