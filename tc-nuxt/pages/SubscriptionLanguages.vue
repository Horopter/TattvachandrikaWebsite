<template>
  <div class="container mx-auto mt-10 px-6">
    <h2 class="text-3xl font-semibold text-gray-900 mb-6">Subscription Languages</h2>

    <!-- Breadcrumb Navigation -->
    <nav aria-label="breadcrumb" class="mb-8">
      <ol class="flex space-x-2 text-gray-600">
        <li>
          <router-link to="/HomePage" class="text-indigo-600 hover:text-indigo-800 font-medium">Home</router-link>
        </li>
        <li>
          <span>/</span>
        </li>
        <li class="text-gray-500 font-medium" aria-current="page">Subscription Languages</li>
      </ol>
    </nav>

    <!-- Subscription Languages Table -->
    <div class="shadow-lg overflow-hidden border border-gray-300 sm:rounded-xl">
      <table class="min-w-full divide-y divide-gray-200">
        <thead class="bg-gray-200">
          <tr>
            <th class="px-6 py-4 text-left text-sm font-semibold text-gray-700 uppercase tracking-wider">Name</th>
            <th class="px-6 py-4 text-left text-sm font-semibold text-gray-700 uppercase tracking-wider">Actions</th>
          </tr>
        </thead>
        <tbody class="bg-white divide-y divide-gray-100">
          <!-- Add New Language Row -->
          <tr v-if="addingNew">
            <td class="px-6 py-4">
              <input type="text" v-model="newSubscriptionLanguage.name" class="border border-gray-300 px-4 py-2 rounded-full w-full focus:ring focus:ring-indigo-300 focus:border-indigo-500" placeholder="Enter language name" />
            </td>
            <td class="px-6 py-4">
              <button class="bg-indigo-600 text-white px-5 py-2 rounded-full shadow-md hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-400 mr-2" @click="saveNewSubscriptionLanguage">Save</button>
              <button class="bg-gray-500 text-white px-5 py-2 rounded-full shadow-md hover:bg-gray-600 focus:outline-none focus:ring-2 focus:ring-gray-300" @click="cancelNewSubscriptionLanguage">Cancel</button>
            </td>
          </tr>

          <!-- Existing Languages Rows -->
          <tr v-for="language in subscriptionLanguages" :key="language._id" class="hover:bg-gray-50 transition duration-150">
            <template v-if="editMode === language._id">
              <td class="px-6 py-4">
                <input type="text" v-model="editSubscriptionLanguage.name" class="border border-gray-300 px-4 py-2 rounded-full w-full focus:ring focus:ring-indigo-300 focus:border-indigo-500" />
              </td>
              <td class="px-6 py-4">
                <button class="bg-indigo-600 text-white px-5 py-2 rounded-full shadow-md hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-400 mr-2" @click="updateSubscriptionLanguage(language._id)">Save</button>
                <button class="bg-gray-500 text-white px-5 py-2 rounded-full shadow-md hover:bg-gray-600 focus:outline-none focus:ring-2 focus:ring-gray-300" @click="cancelEdit">Cancel</button>
              </td>
            </template>
            <template v-else>
              <td class="px-6 py-4 text-md font-semibold text-gray-700 font-sans">{{ language.name }}</td>
              <td class="px-6 py-4 flex items-center space-x-3">
                <button class="bg-yellow-500 text-white px-5 py-2 rounded-full shadow-md hover:bg-yellow-600 focus:outline-none focus:ring-2 focus:ring-yellow-400" @click="editSubscriptionLanguageFunc(language)">Edit</button>
                <button class="bg-red-500 text-white px-5 py-2 rounded-full shadow-md hover:bg-red-600 focus:outline-none focus:ring-2 focus:ring-red-400" @click="showDeleteModal(language._id)">Delete</button>
              </td>
            </template>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Add New Language Button -->
    <div class="mt-6">
      <button class="bg-teal-600 text-white px-6 py-3 rounded-full shadow-md hover:bg-teal-700 focus:outline-none focus:ring-2 focus:ring-teal-400" @click="startAddingNew">Add New Language</button>
    </div>

    <!-- Confirmation Modal -->
    <confirmation-modal
      v-if="showConfirmationModal"
      :show="showConfirmationModal"
      title="Confirm Delete"
      message="Are you sure you want to delete this subscription language?"
      @close="hideDeleteModal"
      @confirm="deleteSubscriptionLanguage"
    />
  </div>
</template>

<script>
import subscriptionLanguageService from '../services/subscriptionLanguageService';
import ConfirmationModal from './ConfirmationModal.vue';

export default {
  components: {
    ConfirmationModal
  },
  data() {
    return {
      subscriptionLanguages: [],
      addingNew: false,
      editMode: null,
      showConfirmationModal: false,
      languageToDelete: null,
      newSubscriptionLanguage: {
        name: ''
      },
      editSubscriptionLanguage: {
        name: ''
      }
    };
  },
  created() {
    this.loadSubscriptionLanguages();
  },
  methods: {
    loadSubscriptionLanguages() {
      subscriptionLanguageService.getSubscriptionLanguages().then(response => {
        this.subscriptionLanguages = response.data;
      }).catch(error => {
        console.error("There was an error retrieving the subscription languages!", error);
      });
    },
    startAddingNew() {
      this.addingNew = true;
      this.resetNewSubscriptionLanguage();
    },
    cancelNewSubscriptionLanguage() {
      this.addingNew = false;
    },
    resetNewSubscriptionLanguage() {
      this.newSubscriptionLanguage = {
        name: ''
      };
    },
    saveNewSubscriptionLanguage() {
      subscriptionLanguageService.createSubscriptionLanguage(this.newSubscriptionLanguage).then(() => {
        this.loadSubscriptionLanguages();
        this.addingNew = false;
      }).catch(error => {
        console.error("There was an error saving the subscription language!", error);
      });
    },
    editSubscriptionLanguageFunc(language) {
      this.editMode = language._id;
      this.editSubscriptionLanguage = { ...language };
    },
    cancelEdit() {
      this.editMode = null;
    },
    updateSubscriptionLanguage(id) {
      subscriptionLanguageService.updateSubscriptionLanguage(id, this.editSubscriptionLanguage).then(() => {
        this.loadSubscriptionLanguages();
        this.editMode = null;
      }).catch(error => {
        console.error("There was an error updating the subscription language!", error);
      });
    },
    showDeleteModal(id) {
      this.languageToDelete = id;
      this.showConfirmationModal = true;
    },
    hideDeleteModal() {
      this.showConfirmationModal = false;
      this.languageToDelete = null;
    },
    deleteSubscriptionLanguage() {
      subscriptionLanguageService.deleteSubscriptionLanguage(this.languageToDelete).then(() => {
        this.loadSubscriptionLanguages();
        this.hideDeleteModal();
      }).catch(error => {
        console.error("There was an error deleting the subscription language!", error);
      });
    }
  }
};
</script>

<style scoped>
/* Add custom styles for smooth hover effects and modern design */
</style>
