function currencyConverter() {
    return {
        amount: 1,
        rates: {},
        symbols: {},
        fromCurrency: '',

        // Config data
        config: {
            title: '',
            cardTitle: '',
            labels: {
                amount: '',
                currency: '',
                footer: ''
            },
            themes: []
        },
        currentTheme: 'dark',

        async init() {
            // Load Config
            try {
                const configRes = await fetch('config.json');
                this.config = await configRes.json();

                // Initialize defaults from config
                if (this.config.defaults) {
                    this.amount = this.config.defaults.amount || 1;
                }
            } catch (error) {
                console.error('Error loading config:', error);
            }

            // Initialize Theme
            const storedTheme = localStorage.getItem('theme');
            if (storedTheme && this.config.themes.includes(storedTheme)) {
                this.currentTheme = storedTheme;
            } else if (this.config.themes.length > 0) {
                this.currentTheme = this.config.themes[0];
            }
            this.applyTheme();

            // Load Rates
            try {
                const ratesRes = await fetch('rates.json');
                const data = await ratesRes.json();

                if (data.rates) {
                    this.rates = data.rates;
                    this.symbols = data.symbols || {};

                    if (data.info && data.info.default_from && this.rates[data.info.default_from]) {
                        this.fromCurrency = data.info.default_from;
                    } else {
                        this.fromCurrency = Object.keys(this.rates)[0] || 'USD';
                    }
                } else {
                    this.rates = data;
                    this.fromCurrency = Object.keys(this.rates)[0] || 'USD';
                }
            } catch (error) {
                console.error('Error fetching rates:', error);
            }

            // Watch for theme changes
            this.$watch('currentTheme', (value) => {
                localStorage.setItem('theme', value);
                this.applyTheme();
            });
        },

        applyTheme() {
            document.documentElement.setAttribute('data-theme', this.currentTheme);
        },

        convert(targetRate) {
            if (!this.amount || !this.fromCurrency || !this.rates[this.fromCurrency]) {
                return '0.0000';
            }

            const fromRate = this.rates[this.fromCurrency];
            const baseAmount = this.amount / fromRate;
            const convertedAmount = baseAmount * targetRate;

            return convertedAmount.toLocaleString(undefined, {
                minimumFractionDigits: 4,
                maximumFractionDigits: 4
            });
        },

        getSymbol(code) {
            return (this.symbols && this.symbols[code]) ? this.symbols[code] : '';
        }
    }
}
