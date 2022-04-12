class myProcessor {
    protected:
        int exp;
        int size;

    public:
        myProcessor(int exp_in, int size_in);
        int process(double *d, int size);
};
