// ckanext-datagov/ckanext/datagov/static/app.js

new Vue({
    el: '#app',
    data: {
        datasets: [],
        loading: true,
        error: null,
    },
    created() {
        this.fetchDatasets();
    },
    methods: {
        async fetchDatasets() {
            try {
                const response = await axios.get('https://datagov-app01.staging.ifad.org/api/3/action/package_search', {
                    params: {
                        q: '',
                        rows: 10
                    }
                });
                this.datasets = response.data.result.results;
                this.updateDynamicContent();
            } catch (err) {
                this.error = err.message;
                this.loading = false;
            }
        },
        updateDynamicContent() {
            const content = document.getElementById('dynamic-content');
            if (this.error) {
                content.innerHTML = `<p>Error: ${this.error}</p>`;
            } else {
                const list = this.datasets.map(dataset => `<li><a href="/dataset/${dataset.id}">${dataset.title}</a></li>`).join('');
                content.innerHTML = `<ul>${list}</ul>`;
            }
            this.loading = false;
        }
    },
});
